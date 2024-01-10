# Bitbucket Pipelines Pipe: Scribe evidence generator

Scribe support evidence collecting and integrity verification for Bitbucket pipelines.

### YAML Definition

Add the following snippet to the script section of your `bitbucket-pipelines.yml` file:

```yaml
- pipe: scribe-security/valint-pipe:1.0.0
  variables:
    COMMAND_NAME: "<string>"  # 'bom', 'slsa' or 'verify'.
    TARGET: "<string>"

    # Common variables
    # VERBOSE: "<boolean>" # Optional
    # CONFIG: "<string>" # Optional
    # FORMAT: "<string>" # Optional
    # INPUT_FORMAT: '<string>' # Optional
    # OUTPUT_DIRECTORY: '<boolean>' # Optional
    # OUTPUT_FILE: '<string>' # Optional
    # LABEL: '<string>' # Optional
    # ENV: '<string>' # Optional
    # FORCE: '<boolean>' # Optional
    # GIT_BRANCH: '<string>' # Optional
    # GIT_COMMIT: '<string>' # Optional
    # GIT_TAG: '<string>' # Optional
    # ATTEST_CONFIG: '<string>' # Optional
    # ATTEST_DEFAULT: '<string>' # Optional Create evidence command
    # SCRIBE_ENABLE: '<string>' # Optional
    # SCRIBE_CLIENT_ID: '<string>' # Optional
    # SCRIBE_CLIENT_SECRET: '<string>' # Optional
    # ATTESTATION: '<string>' # Optional
    # OCI: '<boolean>' # Optional
    # OCI_REPO: '<string>' # Optional
    # BACKOFF: "<string>" # Optional
    # CA: "<string>" # Optional
    # CACHE_ENABLE: "<boolean>" # Optional
    # CERT: "<string>" # Optional
    # CONTEXT_DIR: "<string>" # Optional
    # TIMEOUT: "<string>" # Optional
    # STRUCTURED: "<boolean>" # Optional
    # VERBOSE: "<integer>" # Optional
    #
    # Bom variables
    # COMPRESS: "<boolean>" # Optional
    # COMPONENTS: '<string>' # Optional
    # ATTACH_REGEX: "<string>" # Optional
    # AUTHOR_EMAIL: "<string>" # Optional
    # AUTHOR_NAME: "<string>" # Optional
    # AUTHOR_PHONE: "<string>" # Optional
    # SUPPLIER_EMAIL: "<string>" # Optional
    # SUPPLIER_NAME: "<string>" # Optional
    # SUPPLIER_PHONE: "<string>" # Optional
    # SUPPLIER_URL: "<string>" # Optional
    # FILTER_REGEX: '<string>' # Optional
    # FILTER_SCOPE: '<string>' # Optional
    # PACKAGE_TYPE: '<string>' # Optional
    # PACKAGE_EXCLUDE_TYPE: '<string>' # Optional
    # PACKAGE_GROUP: '<string>' # Optional
    # PREDICATE: "<string>" # Optional
    
    # SLSA variables
    # ALL_ENV: "<boolean>" #Optional
    # BUILD_TYPE: "<string>" #Optional
    # BUILDER_ID: "<string>" #Optional
    # BY_PRODUCT: "<string>" #Optional
    # EXTERNAL: "<string>" #Optional
    # FINISHED_ON: "<string>" #Optional
    # INVOCATION: "<string>" #Optional
    # STARTED_ON: "<string>" #Optional
    # STATEMENT: "<string>" #Optional
    
    # Verify variables
    # ATTESTATION: "<string>" # Optional
    # COMMON_NAME: "<string>" # Optional
    # EMAIL: "<string>" # Optional
    # INPUT_FORMAT: "<string>" # Optional
```

### Required Variables

| Variable     | Usage                                    |
| ------------ | ---------------------------------------- |
| COMMAND_NAME | Name of the command to execute (bom, slsa, verify) |
| TARGET       | Target object name format=`[docker:{image:tag}, dir:{dir_path}, git:{git_path}, docker-archive:{archive_path}, oci-archive:archive_path, registry:image:tag`] |

### Common Variables

| Variable          | Usage                    |
| ----------------- | ------------------------ |
| attest.config     | Attestation config path  |
| attest.default    | Attestation default config, options=[sigstore sigstore-github x509 x509-env] |
| backoff           | Backoff duration         |
| ca                | x509 CA Chain path       |
| cache-enable      | Enable local cache       |
| cert              | x509 Cert path           |
| config            | Configuration file path  |
| context-dir       | Context dir              |
| context-type      | CI context type, options=[jenkins github circleci azure gitlab travis tekton bitbucket local] |
| env               | Environment keys to include in sbom |
| filter-regex      | Filter out files by regex |
| git-branch        | Git branch in the repository |
| git-commit        | Git commit hash in the repository |
| git-tag           | Git tag in the repository |
| key               | x509 Private key path    |
| label             | Add Custom labels        |
| level             | Log depth level, options=[panic fatal error warning info debug trace] |
| log-context       | Attach context to all logs |
| log-file          | Output log to file       |
| oci               | Enable OCI store         |
| oci-repo          | Select OCI custom attestation repo |
| output-directory  | Output directory path    |
| output-file       | Output file name         |
| pipeline-name     | Pipeline name            |
| predicate-type    | Custom Predicate type (generic evidence format) |
| product-key       | Product Key              |
| product-version   | Product Version          |
| quiet             | Suppress all logging output |
| scribe.client-id  | Scribe Client ID         |
| scribe.client-secret | Scribe Client Secret  |
| scribe.enable     | Enable scribe client     |
| scribe.url        | Scribe API Url           |
| structured        | Enable structured logger |
| timeout           | Timeout duration         |
| verbose           | Log verbosity level [-v,--verbose=1] = info, [-vv,--verbose=2] = debug |

### Bom Command Variables

if `COMMAND` is set to `bom`:

| Variable          | Usage                   |
| ----------------- | ----------------------- |
| COMPRESS          | Compress content        |
| COMPONENTS        | Select sbom components groups, options=[metadata layers packages syft files dep commits] |
| ATTACH_REGEX      | Attach files content by regex |
| AUTHOR_EMAIL      | Set author email         |
| AUTHOR_NAME       | Set author name          |
| AUTHOR_PHONE      | Set author phone         |
| SUPPLIER_EMAIL    | Set supplier email       |
| SUPPLIER_NAME     | Set supplier name        |
| SUPPLIER_PHONE    | Set supplier phone       |
| SUPPLIER_URL      | Set supplier URL         |
| FILTER_REGEX      | Filter out files by regex |
| FILTER_SCOPE      | Filter packages by scope |
| PACKAGE_TYPE      | Select package type      |
| PACKAGE_EXCLUDE_TYPE | Exclude package type, options=[ruby python javascript java dpkg apkdb rpm go-mod dotnet r-package rust binary sbom] |
| PACKAGE_GROUP     | Select package group     |
| PREDICATE         | Import predicate path    |

### SLSA Command Variables

if `COMMAND` is set to `slsa`:

| Variable       | Usage                                                          |
| -------------- | -------------------------------------------------------------- |
| ALL_ENV        | Attach all environment variables                              |
| BUILD_TYPE     | Set build type                                                 |
| BUILDER_ID     | Set builder id                                                 |
| BY_PRODUCT     | Attach by product path                                         |
| COMPONENTS     | Select by products components groups, options=[metadata layers packages syft files dep commits] |
| EXTERNAL       | Add build external parameters                                  |
| FINISHED_ON    | Set metadata finished time (YYYY-MM-DDThh:mm:ssZ)              |
| FORCE          | Force overwrite cache                                          |
| FORMAT         | Evidence format, options=[statement attest predicate]          |
| INVOCATION     | Set metadata invocation ID                                     |
| PREDICATE      | Import predicate path                                          |
| STARTED_ON     | Set metadata started time (YYYY-MM-DDThh:mm:ssZ)              |
| STATEMENT      | Import statement path                                          |

### SLSA Command Variables

if `COMMAND` is set to `verify`:

| Variable       | Usage                                                          |
| -------------- | -------------------------------------------------------------- |
| ATTESTATION    | Attestation for target                                         |
| COMMON_NAME    | Default policy allowed common names                            |
| EMAIL          | Default policy allowed emails                                  |
| FORCE          | Force skip cache                                               |
| INPUT_FORMAT   | Evidence format, options=[attest-cyclonedx-json attest-slsa statement-slsa statement-cyclonedx-json statement-generic attest-generic] |
| URI            | Default policy allowed uris                                    |

### Usage

```yaml
 - pipe: scribe-security/valint-pipe:1.0.0
   variables:
    COMMAND_NAME: bom
    TARGET: busybox:latest
    VERBOSE: 2
    FORCE: "true"
```

### Target types - `[target]`

---

Target types are types of artifacts produced and consumed by your supply chain.
Using supported targets, you can collect evidence and verify compliance on a range of artifacts.

> Fields specified as [target] support the following format.

### Format

`[scheme]:[name]:[tag]`

| Sources        | target-type | scheme         | Description                                                     | example                                   |
| -------------- | ----------- | -------------- | --------------------------------------------------------------- | ----------------------------------------- |
| Docker Daemon  | image       | docker         | use the Docker daemon                                           | docker:busybox:latest                     |
| OCI registry   | image       | registry       | use the docker registry directly                                | registry:busybox:latest                   |
| Docker archive | image       | docker-archive | use a tarball from disk for archives created from "docker save" | image                                     |
| OCI archive    | image       | oci-archive    | tarball from disk for OCI archives                              | oci-archive:path/to/yourimage.tar         |
| Remote git     | git         | git            | remote repository git                                           | git:https://github.com/yourrepository.git |
| Local git      | git         | git            | local repository git                                            | git:path/to/yourrepository                |
| Directory      | dir         | dir            | directory path on disk                                          | dir:path/to/yourproject                   |
| File           | file        | file           | file path on disk                                               | file:path/to/yourproject/file             |

### Evidence Stores

Each storer can be used to store, find and download evidence, unifying all the supply chain evidence into a system is an important part to be able to query any subset for policy validation.

| Type   | Description                                 | requirement              |
| ------ | ------------------------------------------- | ------------------------ |
| scribe | Evidence is stored on scribe service        | scribe credentials       |
| OCI    | Evidence is stored on a remote OCI registry | access to a OCI registry |

### Scribe Evidence store

Scribe evidence store allows you store evidence using scribe Service.

Related Flags:

> Note the flag set:
>
> * `SCRIBE_CLIENT_ID`
> * `SCRIBE_CLIENT_ID`
> * `SCRIBE_ENABLE`

### Before you begin

Integrating Scribe Hub with your environment requires the following credentials that are found in the **Integrations** page. (In your **[Scribe Hub](https://scribehub.scribesecurity.com/ "Scribe Hub Link")** go to **integrations**)

* **Client ID**
* **Client Secret**

<img src='assets/integrations-secrets.jpg' alt='Scribe Integration Secrets' width='70%' min-width='400px'/>

* Set your Scribe credentials as environment variables according to **[Bitbucket instructions](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/ "Bitbucket instructions")**.
* Use the Scribe custom pipe as shown in the example bellow

### Usage

```yaml
pipelines:
  default:
    - step:
        name: scribe-bitbucket-pipeline
        script:    
          - pipe: scribe-security/valint-pipe:1.0.0
            variables:
              COMMAND_NAME: bom
              TARGET:  [target]
              FORMAT: [attest, statement, attest-slsa, statement-slsa, attest-generic, statement-generic]
              SCRIBE_ENABLE: true
              SCRIBE_CLIENT_ID: $SCRIBE_CLIENT_ID
              SCRIBE_CLIENT_SECRET: $SCRIBE_CLIENT_SECRET

          - pipe: scribe-security/valint-pipe:1.0.0
            variables:
              COMMAND_NAME: verify
              TARGET:  [target]
              INPUT_FORMAT: [attest, statement, attest-slsa, statement-slsa, attest-generic, statement-generic]
              SCRIBE_ENABLE: true
              SCRIBE_CLIENT_ID: $SCRIBE_CLIENT_ID
              SCRIBE_CLIENT_SECRET: $SCRIBE_CLIENT_SECRET
```

### Alternative evidence stores

> You can learn more about alternative stores **[here](https://scribe-security.netlify.app/docs/integrating-scribe/other-evidence-stores)**.

<details>
  <summary> <b> OCI Evidence store </b></summary>
Valint supports both storage and verification flows for `attestations`  and `statement` objects utilizing OCI registry as an evidence store.

Using OCI registry as an evidence store allows you to upload, download and verify evidence across your supply chain in a seamless manner.

Related flags:

* `OCI` Enable OCI store.
* `OCI_REPO` - Evidence store location.

### Before you begin

Evidence can be stored in any accusable registry.

* Write access is required for upload (generate).
* Read access is required for download (verify).

You must first login with the required access privileges to your registry before calling Valint.
For example, using `docker login` command.

### Usage

```yaml
pipelines:
  default:
    - step:
        name: scribe-bitbucket-oci-pipeline
        script:    
          - docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD [my_registry]
          - pipe: scribe-security/valint-pipe:1.0.0
            variables:
              COMMAND_NAME: bom
              TARGET:  [target]
              FORMAT: [attest, statement, attest-slsa (depricated), statement-slsa(depricated), attest-generic, statement-generic]
              OCI: true
              OCI_REPO: [oci_repo]

          - pipe: scribe-security/valint-pipe:1.0.0
            variables:
              COMMAND_NAME: verify
              TARGET:  [target]
              INPUT_FORMAT: [attest, statement, attest-slsa, statement-slsa, attest-generic, statement-generic]
              OCI: true
              OCI_REPO: [oci_repo]
```

</details>

## Basic examples

### Public registry image (SBOM)

Create SBOM from remote `busybox:latest` image.

```YAML
  - pipe: scribe-security/valint-pipe:1.0.0
      variables:
        COMMAND: bom
        TARGET: busybox:latest
        FORCE: "true"
```

### Public registry image (SLSA)

Create slsa from remote `busybox:latest` image.

```YAML
  - pipe: scribe-security/valint-pipe:1.0.0
      variables:
        COMMAND: slsa
        TARGET: busybox:latest
```

### Docker built image (SBOM)

Create SBOM for image built by local docker `image_name:latest` image.

```YAML
- pipe: scribe-security/valint-pipe:1.0.0
  variables:
    COMMAND: bom
    TARGET: image_name:latest
    VERBOSE: 2
    FORCE: "true"
```

### Docker built image (SLSA)

Create SLSA for image built by local docker `image_name:latest` image.

```YAML
- pipe: scribe-security/valint-pipe:1.0.0
  variables:
    COMMAND: slsa
    TARGET: image_name:latest
    FORCE: "true"
```

### Private registry image (SBOM)

Create SBOM for image hosted on private registry.

> Use `docker login` to add access.

```YAML
- pipe: scribe-security/valint-pipe:1.0.0
  variables:
    COMMAND: bom
    TARGET: scribesecurity.jfrog.io/scribe-docker-local/example:latest
    FORCE: true
```

### Private registry image (SLSA)

Create SLSA for image hosted on private registry.

> Use `docker login` to add access.

```YAML
- pipe: scribe-security/valint-pipe:1.0.0
  variables:
    COMMAND: slsa
    TARGET: scribesecurity.jfrog.io/scribe-docker-local/example:latest
    FORCE: true
    VERBOSE: 2
```

### Custom metadata (SBOM)

Custom metadata added to SBOM.

```YAML
- step:
    name: valint-image-step
    script:
      - export test_env=test_env_value
      - pipe: docker://scribesecuriy.jfrog.io/scribe-docker-public-local/valint-pipe:dev-latest
        variables:
          COMMAND_NAME: bom
          TARGET: busybox:latest
          FORCE: "true"
          ENV: test_env
          LABEL: test_label
```

### Custom metadata (SLSA)

Custom metadata added to SLSA.

```YAML
- step:
    name: valint-image-step
    script:
      - export test_env=test_env_value
      - pipe: docker://scribesecuriy.jfrog.io/scribe-docker-public-local/valint-pipe:dev-latest
        variables:
          COMMAND_NAME: slsa
          TARGET: busybox:latest
          FORCE: "true"
          ENV: test_env
          LABEL: test_label
```

### Save as artifact SBOM

Using input variable `OUTPUT_DIRECTORY` or `OUTPUT_FILE` to export evidence as an artifact.

> Use input variable `FORMAT` to select between supported formats.

```YAML
- step:
    name: save-artifact-step
    script:
      - pipe: docker://scribesecuriy.jfrog.io/scribe-docker-public-local/valint-pipe:dev-latest
        variables:
          COMMAND_NAME: bom
          OUTPUT_FILE: my_sbom.json
          TARGET: busybox:latest
          FORCE: "true"
    artifacts:
      - scribe/**
      - my_sbom.json
```

### Save as artifact SLSA

Using input variable `OUTPUT_DIRECTORY` or `OUTPUT_FILE` to export evidence as an artifact.

> Use input variable `FORMAT` to select between supported formats.

```YAML
- step:
    name: save-artifact-step
    script:
      - pipe: docker://scribesecuriy.jfrog.io/scribe-docker-public-local/valint-pipe:dev-latest
        variables:
          COMMAND_NAME: slsa
          OUTPUT_FILE: my_slsa.json
          TARGET: busybox:latest
          FORCE: "true"
    artifacts:
      - scribe/**
      - my_sbom.json
```

### Directory target (SBOM)

Create SBOM from a local directory.

```YAML
step:
  name: dir-sbom-step
  script:
  - mkdir testdir
  - echo "test" > testdir/test.txt
  - pipe: scribe-security/valint-pipe:1.0.0
    variables:
      COMMAND: bom
      TARGET: dir:./testdir
      SCRIBE_CLIENT_ID: $SCRIBE_CLIENT_ID
      SCRIBE_CLIENT_SECRET: $SCRIBE_CLIENT_SECRET
```

### Directory target (SLSA)

Create SLSA from a local directory.

```YAML
step:
  name: dir-sbom-step
  script:
  - mkdir testdir
  - echo "test" > testdir/test.txt
  - pipe: scribe-security/valint-pipe:1.0.0
    variables:
      COMMAND: slsa
      TARGET: dir:./testdir
      SCRIBE_CLIENT_ID: $SCRIBE_CLIENT_ID
      SCRIBE_CLIENT_SECRET: $SCRIBE_CLIENT_SECRET
```

### Git target (SBOM)

Create SBOM for `mongo-express` remote git repository.

```YAML
- step:
    name: valint-git-step
    script:
      - pipe: docker://scribesecuriy.jfrog.io/scribe-docker-public-local/valint-pipe:dev-latest
        variables:
          COMMAND_NAME: bom
          TARGET: git:https://github.com/mongo-express/mongo-express.git
          VERBOSE: 2
          FORCE: "true"
```

Create SBOM for local git repository.

```YAML
    - step:
        name: valint-git-step
        script:
          - git clone https://github.com/mongo-express/mongo-express.git scm_mongo_express
          - pipe: docker://scribesecuriy.jfrog.io/scribe-docker-public-local/valint-pipe:dev-latest
            variables:
              COMMAND_NAME: bom
              TARGET: dir:scm_mongo_express
              VERBOSE: 2
              FORCE: "true"
```

### Git target (SLSA)

Create SLSA for `mongo-express` remote git repository.

```YAML
- step:
    name: valint-git-step
    script:
      - pipe: docker://scribesecuriy.jfrog.io/scribe-docker-public-local/valint-pipe:dev-latest
        variables:
          COMMAND_NAME: slsa
          TARGET: git:https://github.com/mongo-express/mongo-express.git
          VERBOSE: 2
          FORCE: "true"
```

Create SLSA for local git repository.

```YAML
    - step:
        name: valint-git-step
        script:
          - git clone https://github.com/mongo-express/mongo-express.git scm_mongo_express
          - pipe: docker://scribesecuriy.jfrog.io/scribe-docker-public-local/valint-pipe:dev-latest
            variables:
              COMMAND_NAME: slsa
              TARGET: dir:scm_mongo_express
              VERBOSE: 2
              FORCE: "true"
```

## Resources
If you're new to Bitbucket pipelines this link should help you get started:

[Bitbucket Pipelines](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/ "Get started with Bitbucket Pipelines") - Get started with Bitbucket Pipelines.

## Support

If you'd like help with this pipe, or you have an issue or a feature request, [let us know](https://github.com/scribe-security/valint-pipe/issues).

If you are reporting an issue, please include:

- the version of the pipe
- relevant logs and error messages
- steps to reproduce

By email or slack, 
[Contact-us](https://scribesecurity.com/contact-us/).

## License

Copyright (c) 2019 Atlassian and others.
Apache 2.0 licensed, see [LICENSE](LICENSE.txt) file.