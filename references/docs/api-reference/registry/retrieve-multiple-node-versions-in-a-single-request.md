> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve multiple node versions in a single request



## OpenAPI

````yaml https://api.comfy.org/openapi post /bulk/nodes/versions
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /bulk/nodes/versions:
    post:
      tags:
        - Registry
      summary: Retrieve multiple node versions in a single request
      operationId: GetBulkNodeVersions
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BulkNodeVersionsRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BulkNodeVersionsResponse'
          description: Successfully retrieved node versions
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Bad request, invalid input
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
components:
  schemas:
    BulkNodeVersionsRequest:
      properties:
        node_versions:
          description: List of node ID and version pairs to retrieve
          items:
            $ref: '#/components/schemas/NodeVersionIdentifier'
          type: array
      required:
        - node_versions
      type: object
    BulkNodeVersionsResponse:
      properties:
        node_versions:
          description: List of retrieved node versions with their status
          items:
            $ref: '#/components/schemas/BulkNodeVersionResult'
          type: array
      required:
        - node_versions
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
    NodeVersionIdentifier:
      properties:
        node_id:
          description: The unique identifier of the node
          type: string
        version:
          description: The version of the node
          type: string
      required:
        - node_id
        - version
      type: object
    BulkNodeVersionResult:
      properties:
        error_message:
          description: Error message if retrieval failed (only present if status is error)
          type: string
        identifier:
          $ref: '#/components/schemas/NodeVersionIdentifier'
        node_version:
          $ref: '#/components/schemas/NodeVersion'
        status:
          description: Status of the retrieval operation
          enum:
            - success
            - not_found
            - error
          type: string
      required:
        - identifier
        - status
      type: object
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
    NodeVersionStatus:
      enum:
        - NodeVersionStatusActive
        - NodeVersionStatusDeleted
        - NodeVersionStatusBanned
        - NodeVersionStatusPending
        - NodeVersionStatusFlagged
      type: string

````