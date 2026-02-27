> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Post proxyvidustart end2video



## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/vidu/start-end2video
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/vidu/start-end2video:
    post:
      tags:
        - API Nodes
        - Released
      operationId: ViduStartEnd2Video
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ViduTaskRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ViduTaskReply'
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
    ViduTaskRequest:
      properties:
        aspect_ratio:
          type: string
        audio:
          description: >-
            Enable direct audio-video generation capability (default true for q3
            model)
          type: boolean
        audio_type:
          description: >-
            Audio type when audio is true: all (sound effects + vocals),
            speech_only, sound_effect_only. Ineffective for q3 model
          enum:
            - all
            - speech_only
            - sound_effect_only
          type: string
        bgm:
          description: Add background music to generated video (ineffective for q3 model)
          type: boolean
        callback_url:
          description: Callback URL for task status updates
          type: string
        duration:
          description: >-
            Video duration in seconds. viduq3-pro: 1-16, viduq2-pro-fast: 1-10,
            viduq2-pro/turbo: 1-8
          format: int32
          type: integer
        enhance:
          type: boolean
        images:
          description: Images for img2video (accepts 1 image as start frame)
          items:
            type: string
          type: array
        is_rec:
          description: Use recommended prompt (consumes additional 10 credits)
          type: boolean
        meta_data:
          description: Metadata identification, JSON format string for custom metadata
          type: string
        model:
          description: >-
            Model name: viduq3-pro, viduq2-pro-fast, viduq2-pro, viduq2-turbo,
            viduq1, viduq1-classic, vidu2.0
          type: string
        movement_amplitude:
          description: >-
            Movement amplitude of objects in frame (ineffective for q2, q3
            models)
          enum:
            - auto
            - small
            - medium
            - large
          type: string
        off_peak:
          description: Off peak mode (lower cost, tasks generated within 48 hours)
          type: boolean
        payload:
          description: Transparent transmission parameters (max 1048576 characters)
          type: string
        priority:
          format: int32
          type: integer
        prompt:
          description: Text prompt for video generation (max 2000 characters)
          type: string
        resolution:
          description: >-
            Resolution: 360p, 540p, 720p, 1080p, 2K (availability depends on
            model and duration)
          type: string
        seed:
          description: Random seed (defaults to random if not specified)
          format: int32
          type: integer
        style:
          enum:
            - general
            - anime
          type: string
        voice_id:
          description: Voice ID for audio (ineffective for q3 model)
          type: string
        watermark:
          description: Add watermark to video (default false)
          type: boolean
        wm_position:
          description: >-
            Watermark position: 1 (top left), 2 (top right), 3 (bottom right,
            default), 4 (bottom left)
          format: int32
          type: integer
        wm_url:
          description: Watermark image URL (uses default watermark if not provided)
          type: string
      type: object
    ViduTaskReply:
      properties:
        aspect_ratio:
          type: string
        bgm:
          description: Whether background music was added
          type: boolean
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
        movement_amplitude:
          enum:
            - auto
            - small
            - medium
            - large
          type: string
        off_peak:
          description: Off peak mode status
          type: boolean
        payload:
          description: Transparent transmission parameters
          type: string
        prompt:
          type: string
        resolution:
          type: string
        seed:
          format: int32
          type: integer
        state:
          $ref: '#/components/schemas/ViduState'
        style:
          enum:
            - general
            - anime
          type: string
        task_id:
          type: string
        watermark:
          description: Whether watermark was added
          type: boolean
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