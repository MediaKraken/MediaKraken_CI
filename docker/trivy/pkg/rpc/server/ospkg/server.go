package ospkg

import (
	"context"

	"github.com/google/wire"
	"golang.org/x/xerrors"

	detector "github.com/aquasecurity/trivy/pkg/detector/ospkg"
	"github.com/aquasecurity/trivy/pkg/log"
	"github.com/aquasecurity/trivy/pkg/rpc"
	"github.com/aquasecurity/trivy/pkg/vulnerability"
	proto "github.com/aquasecurity/trivy/rpc/detector"
)

var SuperSet = wire.NewSet(
	detector.SuperSet,
	vulnerability.SuperSet,
	NewServer,
)

type Server struct {
	detector   detector.Operation
	vulnClient vulnerability.Operation
}

func NewServer(detector detector.Operation, vulnClient vulnerability.Operation) *Server {
	return &Server{detector: detector, vulnClient: vulnClient}
}

func (s *Server) Detect(ctx context.Context, req *proto.OSDetectRequest) (res *proto.DetectResponse, err error) {
	vulns, eosl, err := s.detector.Detect(req.OsFamily, req.OsName, rpc.ConvertFromRpcPkgs(req.Packages))
	if err != nil {
		err = xerrors.Errorf("failed to detect vulnerabilities of OS packages: %w", err)
		log.Logger.Error(err)
		return nil, err
	}

	s.vulnClient.FillInfo(vulns, false)

	return &proto.DetectResponse{Vulnerabilities: rpc.ConvertToRpcVulns(vulns), Eosl: eosl}, nil
}
