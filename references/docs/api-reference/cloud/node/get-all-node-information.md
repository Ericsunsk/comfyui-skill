> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all node information

> Returns information about all available nodes



## OpenAPI

````yaml openapi-cloud.yaml get /api/object_info
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
  /api/object_info:
    get:
      tags:
        - node
      summary: Get all node information
      description: Returns information about all available nodes
      operationId: getNodeInfo
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  $ref: '#/components/schemas/NodeInfo'
components:
  schemas:
    NodeInfo:
      type: object
      properties:
        input:
          type: object
          description: Input specifications for the node
          additionalProperties: true
        input_order:
          type: object
          description: Order of inputs for display
          additionalProperties:
            type: array
            items:
              type: string
        output:
          type: array
          items:
            type: string
          description: Output types of the node
        output_is_list:
          type: array
          items:
            type: boolean
          description: Whether each output is a list
        output_name:
          type: array
          items:
            type: string
          description: Names of the outputs
        name:
          type: string
          description: Internal name of the node
        display_name:
          type: string
          description: Display name of the node
        description:
          type: string
          description: Description of the node
        python_module:
          type: string
          description: Python module implementing the node
        category:
          type: string
          description: Category of the node
        output_node:
          type: boolean
          description: Whether this is an output node
        output_tooltips:
          type: array
          items:
            type: string
          description: Tooltips for outputs
        deprecated:
          type: boolean
          description: Whether the node is deprecated
        experimental:
          type: boolean
          description: Whether the node is experimental
        api_node:
          type: boolean
          description: Whether this is an API node
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