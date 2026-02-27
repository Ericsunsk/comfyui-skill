> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Post proxyviduextend



## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/vidu/extend
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/vidu/extend:
    post:
      tags:
        - API Nodes
        - Released
      operationId: ViduExtend
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ViduExtendRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ViduExtendReply'
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
    ViduExtendRequest:
      properties:
        callback_url:
          description: Callback URL for task status updates
          type: string
        duration:
          description: Extended duration in seconds (1-7, default 5)
          format: int32
          type: integer
        images:
          description: Extended reference image to the end frame (only accepts 1 image)
          items:
            type: string
          type: array
        model:
          description: Model name (viduq2-pro or viduq2-turbo)
          type: string
        payload:
          description: Transparent transmission parameters (max 1048576 characters)
          type: string
        prompt:
          description: Text prompt for video generation (max 2000 characters)
          type: string
        resolution:
          description: Resolution (540p, 720p, 1080p)
          type: string
        video_creation_id:
          description: Vidu video_creation_id, required with video_url
          type: string
        video_url:
          description: Any video URL, required with video_creation_id
          type: string
      required:
        - model
      type: object
    ViduExtendReply:
      properties:
        created_at:
          format: date-time
          type: string
        credits:
          format: int32
          type: integer
        duration:
          format: int32
          type: integer
        images:
          items:
            type: string
          type: array
        model:
          type: string
        payload:
          type: string
        prompt:
          type: string
        resolution:
          type: string
        state:
          $ref: '#/components/schemas/ViduState'
        task_id:
          type: string
        video_creation_id:
          type: string
        video_url:
          type: string
      required:
        - task_id
        - state
        - credits
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
    ViduState:
      enum:
        - created
        - processing
        - queueing
        - success
        - failed
      type: string

````