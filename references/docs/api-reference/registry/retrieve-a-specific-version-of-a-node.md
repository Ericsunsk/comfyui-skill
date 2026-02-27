> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a specific version of a node



## OpenAPI

````yaml https://api.comfy.org/openapi get /nodes/{nodeId}/versions/{versionId}
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /nodes/{nodeId}/versions/{versionId}:
    get:
      tags:
        - Registry
      summary: Retrieve a specific version of a node
      operationId: GetNodeVersion
      parameters:
        - in: path
          name: nodeId
          required: true
          schema:
            type: string
        - description: The version of the node. (Not a UUID).
          in: path
          name: versionId
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NodeVersion'
          description: Detailed information about a specific node version
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
          description: Node version not found
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
components:
  schemas:
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
    Error:
      properties:
        details:
          description: >-
            Optional detailed information about the error or hints for resolving
            it.
          items:
            type: string
          type: array
        message:
          description: A clear and concise description of the error.
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
    NodeVersionStatus:
      enum:
        - NodeVersionStatusActive
        - NodeVersionStatusDeleted
        - NodeVersionStatusBanned
        - NodeVersionStatusPending
        - NodeVersionStatusFlagged
      type: string

````