> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# List all node versions given some filters.



## OpenAPI

````yaml https://api.comfy.org/openapi get /versions
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /versions:
    get:
      tags:
        - Registry
      summary: List all node versions given some filters.
      operationId: ListAllNodeVersions
      parameters:
        - in: query
          name: nodeId
          schema:
            type: string
        - explode: true
          in: query
          name: statuses
          schema:
            items:
              $ref: '#/components/schemas/NodeVersionStatus'
            type: array
          style: form
        - in: query
          name: include_status_reason
          schema:
            default: false
            type: boolean
        - description: The page number to retrieve.
          in: query
          name: page
          schema:
            default: 1
            type: integer
        - description: The number of items to include per page.
          in: query
          name: pageSize
          schema:
            default: 10
            type: integer
        - description: search for status_reason, case insensitive
          in: query
          name: status_reason
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  page:
                    description: Current page number
                    type: integer
                  pageSize:
                    description: Maximum number of node versions per page. Maximum is 100.
                    type: integer
                  total:
                    description: Total number of node versions available
                    type: integer
                  totalPages:
                    description: Total number of pages available
                    type: integer
                  versions:
                    items:
                      $ref: '#/components/schemas/NodeVersion'
                    type: array
                type: object
          description: List of all node versions
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Invalid input, object invalid
        '403':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Node banned
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
components:
  schemas:
    NodeVersionStatus:
      enum:
        - NodeVersionStatusActive
        - NodeVersionStatusDeleted
        - NodeVersionStatusBanned
        - NodeVersionStatusPending
        - NodeVersionStatusFlagged
      type: string
    NodeVersion:
      properties:
        changelog:
          description: Summary of changes made in this version
          type: string
        comfy_node_extract_status:
          description: The status of comfy node extraction process.
          type: string
        createdAt:
          description: The date and time the version was created.
          format: date-time
          type: string
        dependencies:
          description: A list of pip dependencies required by the node.
          items:
            type: string
          type: array
        deprecated:
          description: Indicates if this version is deprecated.
          type: boolean
        downloadUrl:
          description: '[Output Only] URL to download this version of the node'
          type: string
        id:
          type: string
        node_id:
          description: The unique identifier of the node.
          type: string
        status:
          $ref: '#/components/schemas/NodeVersionStatus'
        status_reason:
          type: string
        supported_accelerators:
          description: >-
            List of accelerators (e.g. CUDA, DirectML, ROCm) that this node
            supports
          items:
            type: string
          type: array
        supported_comfyui_frontend_version:
          description: Supported versions of ComfyUI frontend
          type: string
        supported_comfyui_version:
          description: Supported versions of ComfyUI
          type: string
        supported_os:
          description: List of operating systems that this node supports
          items:
            type: string
          type: array
        tags:
          items:
            type: string
          type: array
        tags_admin:
          description: Admin-only tags for security warnings and admin metadata
          items:
            type: string
          type: array
        version:
          description: >-
            The version identifier, following semantic versioning. Must be
            unique for the node.
          type: string
      type: object
    ErrorResponse:
      properties:
        error:
          type: string
        message:
          type: string
      required:
        - error
        - message
      type: object

````