# Bitbucket Pipelines Pipe: scribe-cli

secure your code

## YAML Definition

Add the following snippet to the script section of your `bitbucket-pipelines.yml` file:

```yaml
- pipe: scribe-security/scribe-pipe:0.0.0
  variables:
    COMMAND_NAME: "<string>"
    # DEBUG: "<boolean>" # Optional
```
## Variables

| Variable              | Usage                                                       |
| --------------------- | ----------------------------------------------------------- |
| COMMAND_NAME | Name of the command to execute (bom, verify, report) |
| CONFIG | Config of the application |
| CONTEXT_TYPE | Context type, options=[jenkins github circleci local gitlab] |
| INTEGRITY | Select report integrity, options=[Modified Not_Covered Validated Not_Validated] |
| LABEL |  Add custom labels |
| LEVEL | Log level, options=[panic fatal error warning info debug trace] |
| OUTPUT_DIRECTORY | Output directory path |
| OUTPUT_FILE | Output file path |
| PRODUCT_KEY | Scribe project key |
| QUIET |  Suppress all logging output |
| SCRIBE_CLIENT_ID | Scribe client id |
| SCRIBE_CLIENT_SECRET |  Scribe client secret |
| SCRIBE_ENABLE |  Enable scribe client |
| SCRIBE_URL |  Scribe url |
| SCRIBE_LOGIN_URL |  Scribe login url |
| SCRIBE_AUDIENCE |  Scribe AUDIENCE |
| SECTION | Select report sections, options=[files packages packages-files summary] |
| SHOW | Print report to stdout |
| TARGET |  download report from scribe service |
| VERBOSE | Increase verbosity (-v = info, -vv = debug) |
| ATTACH_REGEX | Attach files content by regex |
| ATTEST_CONFIG | Attestation config path |
| ATTEST_DEFAULT | Attestation default config, options=[sigstore sigstore-github x509 kms] |
| ATTEST_NAME | Attestation config name |
| COMPONENTS | Select sbom components groups, options=[metadata layers packages syft files dep] |
| ENV | Envrionment keys to include in sbom |
| FAILONERROR | Fail on errors |
| FILTER_REGEX | Filter out files by regex |
| FORCE | Force overwrite cache |
| FORMAT | Sbom formatter, options=[cyclonedx-json cyclonedx-xml attest-cyclonedx-json statement-cyclonedx-json predicate-cyclonedx-json attest-slsa statement-slsa predicate-slsa] |
| ATTESTATION | Attestation for target |
| INPUT_FORMAT | Sbom input formatter, options=[attest-cyclonedx-json attest-slsa] |


_(*) = required variable._

## Prerequisites

## Examples

Basic example:

```yaml
script:
  - pipe: scribe-security/scribe-pipe:0.0.0
    variables:
      COMMAND_NAME: "bom"
      TARGET: "repo_name"
```

Advanced example:

```yaml
script:
  - pipe: scribe-security/scribe-pipe:0.0.0
    variables:
      COMMAND_NAME: "bom"
      TARGET: "repo_name"
```

## Support
If you’d like help with this pipe, or you have an issue or feature request, let us know.
The pipe is maintained by scribe-security@scribesecurity.com.

If you’re reporting an issue, please include:

- the version of the pipe
- relevant logs and error messages
- steps to reproduce
