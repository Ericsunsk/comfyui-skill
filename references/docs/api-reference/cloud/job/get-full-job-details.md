> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get full job details

> Retrieve complete details for a specific job including workflow and outputs.
Used for detail views, workflow re-execution, and debugging.




## OpenAPI

````yaml openapi-cloud.yaml get /api/jobs/{job_id}
openapi: 3.0.3
info:
  title: Comfy Cloud API
  description: >
    <Warning>

    **Experimental API:** This API is experimental and subject to change. 

    Endpoints, request/response formats, and behavior may be modified without
    notice.

    </Warning>


    API for Comfy Cloud - Run ComfyUI workflows on cloud infrastructure.


    This API allows you to interact with Comfy Cloud programmatically,
    including:

    - Submitting and managing workflows

    - Uploading and downloading files

    - Monitoring job status and progress


    ## Cloud vs OSS ComfyUI Compatibility


    Comfy Cloud implements the same API interfaces as OSS ComfyUI for maximum
    compatibility,

    but some fields are accepted for compatibility while being handled
    differently or ignored:


    | Field | Endpoints | Cloud Behavior |

    |-------|-----------|----------------|

    | `subfolder` | `/api/view`, `/api/upload/*` | **Ignored** - Cloud uses
    content-addressed storage (hash-based). Returned in responses for
    client-side organization. |

    | `type` (input/output/temp) | `/api/view`, `/api/upload/*` | Partially used
    - All files stored with tag-based organization rather than directory
    structure. |

    | `overwrite` | `/api/upload/*` | **Ignored** - Content-addressed storage
    means identical content always has the same hash. |

    | `number`, `front` | `/api/prompt` | **Ignored** - Cloud uses its own fair
    queue scheduling per user. |

    | `split`, `full_info` | `/api/userdata` | **Ignored** - Cloud always
    returns full file metadata. |


    These fields are retained in the API schema for drop-in compatibility with
    existing ComfyUI clients and workflows.
  version: 1.0.0
  license:
    name: GNU General Public License v3.0
    url: https://github.com/comfyanonymous/ComfyUI/blob/master/LICENSE
servers:
  - url: https://cloud.comfy.org
    description: Comfy Cloud API
security:
  - ApiKeyAuth: []
tags:
  - name: workflow
    description: |
      Submit workflows for execution and manage the execution queue.
      This is the primary way to run ComfyUI workflows on the cloud.
  - name: job
    description: |
      Monitor job status, view execution history, and manage running jobs.
      Jobs are created when you submit a workflow via POST /api/prompt.
  - name: asset
    description: |
      Upload, download, and manage persistent assets (images, models, outputs).
      Assets provide durable storage with tagging and metadata support.
  - name: file
    description: |
      Legacy file upload and download endpoints compatible with local ComfyUI.
      For new integrations, consider using the Assets API instead.
  - name: model
    description: |
      Browse available AI models. Models are pre-loaded on cloud infrastructure.
  - name: node
    description: |
      Get information about available ComfyUI nodes and their inputs/outputs.
      Useful for building dynamic workflow interfaces.
  - name: user
    description: |
      User account information and personal data storage.
  - name: system
    description: |
      Server status, health checks, and system information.
paths:
  /api/jobs/{job_id}:
    get:
      tags:
        - job
      summary: Get full job details
      description: >
        Retrieve complete details for a specific job including workflow and
        outputs.

        Used for detail views, workflow re-execution, and debugging.
      operationId: getJobDetail
      parameters:
        - name: job_id
          in: path
          required: true
          description: Job identifier (UUID)
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Success - Job details retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JobDetailResponse'
        '401':
          description: Unauthorized - Authentication required
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '403':
          description: Forbidden - Job does not belong to user
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Job not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    JobDetailResponse:
      type: object
      description: Full job details including workflow and outputs
      required:
        - id
        - status
        - create_time
        - update_time
      properties:
        id:
          type: string
          format: uuid
          description: Unique job identifier
        status:
          type: string
          enum:
            - pending
            - in_progress
            - completed
            - failed
            - cancelled
          description: User-friendly job status
        workflow:
          type: object
          description: Full ComfyUI workflow (10-100KB, omitted if not available)
          additionalProperties: true
        execution_error:
          $ref: '#/components/schemas/ExecutionError'
          description: >-
            Detailed execution error from ComfyUI (only for failed jobs with
            structured error data)
        create_time:
          type: integer
          format: int64
          description: Job creation timestamp (Unix timestamp in seconds)
        update_time:
          type: integer
          format: int64
          description: Last update timestamp (Unix timestamp in seconds)
        outputs:
          type: object
          description: Full outputs object from ComfyUI (only for terminal states)
          additionalProperties: true
        preview_output:
          type: object
          description: Primary preview output (only for terminal states)
          additionalProperties: true
        outputs_count:
          type: integer
          description: Total number of output files (omitted for non-terminal states)
        workflow_id:
          type: string
          description: UUID identifying the workflow graph definition
        execution_status:
          type: object
          description: ComfyUI execution status and timeline (only for terminal states)
          additionalProperties: true
        execution_meta:
          type: object
          description: Node-level execution metadata (only for terminal states)
          additionalProperties: true
    ErrorResponse:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: string
        message:
          type: string
    ExecutionError:
      type: object
      description: Detailed execution error information from ComfyUI
      required:
        - node_id
        - node_type
        - exception_message
        - exception_type
        - traceback
        - current_inputs
        - current_outputs
      properties:
        node_id:
          type: string
          description: ID of the node that failed
        node_type:
          type: string
          description: Type name of the node (e.g., "KSampler")
        exception_message:
          type: string
          description: Human-readable error message
        exception_type:
          type: string
          description: Python exception type (e.g., "RuntimeError")
        traceback:
          type: array
          items:
            type: string
          description: Array of traceback lines (empty array if not available)
        current_inputs:
          type: object
          additionalProperties: true
          description: Input values at time of failure (empty object if not available)
        current_outputs:
          type: object
          additionalProperties: true
          description: Output values at time of failure (empty object if not available)
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: >
        API key authentication. Generate an API key from your account settings

        at https://platform.comfy.org/profile/api-keys. Pass the key in the
        X-API-Key header.

````