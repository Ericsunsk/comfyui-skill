> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Post proxyvidumultiframe



## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/vidu/multiframe
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/vidu/multiframe:
    post:
      tags:
        - API Nodes
        - Released
      operationId: ViduMultiframe
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ViduMultiframeRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ViduMultiframeReply'
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
    ViduMultiframeRequest:
      properties:
        callback_url:
          description: Callback URL for task status updates
          type: string
        image_settings:
          description: Configuration for intelligent multi-frame generation (2-9 frames)
          items:
            $ref: '#/components/schemas/ViduImageSetting'
          type: array
        model:
          description: Model name (viduq2-pro or viduq2-turbo)
          type: string
        payload:
          description: Transparent transmission parameters (max 1048576 characters)
          type: string
        resolution:
          description: Video resolution (540p, 720p, 1080p)
          type: string
        start_image:
          description: The first frame image (Base64 or URL)
          type: string
      required:
        - model
        - start_image
        - image_settings
      type: object
    ViduMultiframeReply:
      properties:
        created_at:
          format: date-time
          type: string
        credits:
          format: int32
          type: integer
        image_settings:
          items:
            $ref: '#/components/schemas/ViduImageSetting'
          type: array
        model:
          type: string
        payload:
          type: string
        resolution:
          type: string
        start_image:
          type: string
        state:
          $ref: '#/components/schemas/ViduState'
        task_id:
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
    ViduImageSetting:
      properties:
        duration:
          description: Duration between key frames in seconds (2-7, default 5)
          format: int32
          type: integer
        key_image:
          description: Reference image for each key frame
          type: string
        prompt:
          description: Prompt for extending the previous frame
          type: string
      required:
        - key_image
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