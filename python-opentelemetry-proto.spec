Name:           python-opentelemetry-proto
# Pinned to 1.39.1 to match the rest of the OpenTelemetry stack (the base
# opentelemetry-api is 1.39.1). The exporter packages pin opentelemetry-proto to
# their own exact version, so it tracks them rather than the latest PyPI release.
# The protobuf runtime pin (>=5.0,<7.0) is satisfied by our protobuf 6.33.5.
Version:        1.39.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenTelemetry Python Proto

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-proto
Source:         %{pypi_source opentelemetry_proto}

BuildArch:      noarch
BuildRequires:  python3-devel
# The package ships generated gRPC service stubs (the *_pb2_grpc modules) that
# import grpc at module load. grpc is optional at runtime (opentelemetry-proto
# declares only protobuf; consumers get grpcio via the proto-grpc exporter), so
# the automatic dependency generator does not add it to Requires. It is pulled in
# here only so the import check exercises those stub modules instead of skipping
# them.
BuildRequires:  python3dist(grpcio)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-proto' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-opentelemetry-proto
Summary:        %{summary}

%description -n python3-opentelemetry-proto %_description


%prep
%autosetup -p1 -n opentelemetry_proto-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l opentelemetry


%check
%pyproject_check_import


%files -n python3-opentelemetry-proto -f %{pyproject_files}


%changelog
%autochangelog
