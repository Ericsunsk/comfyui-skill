> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get release notes

> Fetch release notes from Strapi with caching



## OpenAPI

````yaml https://api.comfy.org/openapi get /releases
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /releases:
    get:
      tags:
        - Releases
      summary: Get release notes
      description: Fetch release notes from Strapi with caching
      operationId: GetReleaseNotes
      parameters:
        - description: The project to get release notes for
          in: query
          name: project
          required: true
          schema:
            enum:
              - comfyui
              - comfyui_frontend
              - desktop
              - cloud
            type: string
        - description: The current version to filter release notes
          in: query
          name: current_version
          schema:
            type: string
        - description: The locale for the release notes
          in: query
          name: locale
          schema:
            default: en
            enum:
              - en
              - es
              - fr
              - ja
              - ko
              - ru
              - zh
            type: string
        - description: The platform requesting the release notes
          in: query
          name: form_factor
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/ReleaseNote'
                type: array
          description: Release notes retrieved successfully
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Bad request
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: Internal server error
components:
  schemas:
    ReleaseNote:
      properties:
        attention:
          description: The attention level for this release
          enum:
            - low
            - medium
            - high
          type: string
        content:
          description: The content of the release note in markdown format
          type: string
        id:
          description: Unique identifier for the release note
          type: integer
        project:
          description: The project this release note belongs to
          enum:
            - comfyui
            - comfyui_frontend
            - desktop
            - cloud
          type: string
        published_at:
          description: When the release note was published
          format: date-time
          type: string
        version:
          description: The version of the release
          type: string
      required:
        - id
        - project
        - version
        - attention
        - content
        - published_at
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