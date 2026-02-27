> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get proxyvidutasks creations



## OpenAPI

````yaml https://api.comfy.org/openapi get /proxy/vidu/tasks/{id}/creations
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/vidu/tasks/{id}/creations:
    get:
      tags:
        - API Nodes
        - Released
      operationId: ViduGetCreations
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ViduGetCreationsReply'
          description: OK
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
          description: Error 4xx/5xx
        default:
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
          description: Error 4xx/5xx
components:
  schemas:
    ViduGetCreationsReply:
      properties:
        creations:
          items:
            $ref: '#/components/schemas/ViduCreation'
          type: array
        err_code:
          type: string
        id:
          type: string
        state:
          $ref: '#/components/schemas/ViduState'
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
    ViduCreation:
      properties:
        cover_url:
          type: string
        id:
          type: string
        moderation_url:
          items:
            type: string
          type: array
        url:
          type: string
        watermarked_url:
          type: string
      type: object
    ViduState:
      enum:
        - created
        - processing
        - queueing
        - success
        - failed
      type: string

````