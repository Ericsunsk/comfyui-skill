> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Add review to a specific version of a node



## OpenAPI

````yaml https://api.comfy.org/openapi post /nodes/{nodeId}/reviews
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /nodes/{nodeId}/reviews:
    post:
      tags:
        - Registry
      summary: Add review to a specific version of a node
      operationId: PostNodeReview
      parameters:
        - in: path
          name: nodeId
          required: true
          schema:
            type: string
        - description: number of star given to the node version
          in: query
          name: star
          required: true
          schema:
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Node'
          description: Detailed information about a specific node
        '400':
          description: Bad Request
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
    Node:
      properties:
        author:
          type: string
        banner_url:
          description: URL to the node's banner.
          type: string
        category:
          deprecated: true
          description: >-
            DEPRECATED: The category of the node. Use 'tags' field instead. This
            field will be removed in a future version.
          type: string
        created_at:
          description: The date and time when the node was created
          format: date-time
          type: string
        description:
          type: string
        downloads:
          description: The number of downloads of the node.
          type: integer
        github_stars:
          description: Number of stars on the GitHub repository.
          type: integer
        icon:
          description: URL to the node's icon.
          type: string
        id:
          description: The unique identifier of the node.
          type: string
        latest_version:
          $ref: '#/components/schemas/NodeVersion'
        license:
          description: The path to the LICENSE file in the node's repository.
          type: string
        name:
          description: The display name of the node.
          type: string
        preempted_comfy_node_names:
          description: A list of Comfy node names that are preempted by this node.
          items:
            type: string
          type: array
        publisher:
          $ref: '#/components/schemas/Publisher'
        rating:
          description: The average rating of the node.
          type: number
        repository:
          description: URL to the node's repository.
          type: string
        search_ranking:
          description: >-
            A numerical value representing the node's search ranking, used for
            sorting search results.
          type: integer
        status:
          $ref: '#/components/schemas/NodeStatus'
        status_detail:
          description: The status detail of the node.
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
        translations:
          additionalProperties:
            additionalProperties: true
            type: object
          description: Translations of node metadata in different languages.
          type: object
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
    Publisher:
      properties:
        createdAt:
          description: The date and time the publisher was created.
          format: date-time
          type: string
        description:
          type: string
        id:
          description: >-
            The unique identifier for the publisher. It's akin to a username.
            Should be lowercase.
          type: string
        logo:
          description: URL to the publisher's logo.
          type: string
        members:
          description: A list of members in the publisher.
          items:
            $ref: '#/components/schemas/PublisherMember'
          type: array
        name:
          type: string
        source_code_repo:
          type: string
        status:
          $ref: '#/components/schemas/PublisherStatus'
        support:
          type: string
        website:
          type: string
      type: object
    NodeStatus:
      enum:
        - NodeStatusActive
        - NodeStatusDeleted
        - NodeStatusBanned
      type: string
    NodeVersionStatus:
      enum:
        - NodeVersionStatusActive
        - NodeVersionStatusDeleted
        - NodeVersionStatusBanned
        - NodeVersionStatusPending
        - NodeVersionStatusFlagged
      type: string
    PublisherMember:
      properties:
        id:
          description: The unique identifier for the publisher member.
          type: string
        role:
          description: The role of the user in the publisher.
          type: string
        user:
          $ref: '#/components/schemas/PublisherUser'
      type: object
    PublisherStatus:
      enum:
        - PublisherStatusActive
        - PublisherStatusBanned
      type: string
    PublisherUser:
      properties:
        email:
          description: The email address for this user.
          type: string
        id:
          description: The unique id for this user.
          type: string
        name:
          description: The name for this user.
          type: string
      type: object

````