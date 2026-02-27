> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Upscale an image with Magnific

> This asynchronous endpoint enables image upscaling using advanced AI algorithms.
Upon submission, it returns a unique task_id which can be used to track the progress.
For real-time production use, include the optional webhook_url parameter to receive
an automated notification once the task has been completed.




## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/freepik/v1/ai/image-upscaler
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/freepik/v1/ai/image-upscaler:
    post:
      tags:
        - Freepik
        - Proxy
      summary: Upscale an image with Magnific
      description: >
        This asynchronous endpoint enables image upscaling using advanced AI
        algorithms.

        Upon submission, it returns a unique task_id which can be used to track
        the progress.

        For real-time production use, include the optional webhook_url parameter
        to receive

        an automated notification once the task has been completed.
      operationId: FreepikMagnificUpscalerCreative
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FreepikMagnificUpscalerCreativeRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikTaskResponse'
          description: OK - The upscaling process has started
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikErrorResponse'
          description: Bad Request
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikErrorResponse'
          description: Internal Server Error
      security:
        - BearerAuth: []
components:
  schemas:
    FreepikMagnificUpscalerCreativeRequest:
      properties:
        creativity:
          default: 0
          description: Increase or decrease AI's creativity. Valid values range [-10, 10].
          maximum: 10
          minimum: -10
          type: integer
        engine:
          default: automatic
          description: Magnific model engines.
          enum:
            - automatic
            - magnific_illusio
            - magnific_sharpy
            - magnific_sparkle
          type: string
        fractality:
          default: 0
          description: >-
            Control the strength of the prompt and intricacy per square pixel.
            Valid values range [-10, 10].
          maximum: 10
          minimum: -10
          type: integer
        hdr:
          default: 0
          description: >-
            Increase or decrease the level of definition and detail. Valid
            values range [-10, 10].
          maximum: 10
          minimum: -10
          type: integer
        image:
          description: >-
            Base64 image or URL to upscale. The resulted image can't exceed
            maximum allowed size of 25.3 million pixels.
          type: string
        optimized_for:
          default: standard
          description: Styles to optimize the upscale process.
          enum:
            - standard
            - soft_portraits
            - hard_portraits
            - art_n_illustration
            - videogame_assets
            - nature_n_landscapes
            - films_n_photography
            - 3d_renders
            - science_fiction_n_horror
          type: string
        prompt:
          description: >-
            Prompt to guide the upscale process. Reusing the same prompt for
            AI-generated images will improve the results.
          type: string
        resemblance:
          default: 0
          description: >-
            Adjust the level of resemblance to the original image. Valid values
            range [-10, 10].
          maximum: 10
          minimum: -10
          type: integer
        scale_factor:
          default: 2x
          description: >-
            Configure scale factor of the image. For higher scales, the image
            will take longer to process.
          enum:
            - 2x
            - 4x
            - 8x
            - 16x
          type: string
        webhook_url:
          description: >-
            Optional callback URL that will receive asynchronous notifications
            whenever the task changes status.
          example: https://www.example.com/webhook
          format: uri
          type: string
      required:
        - image
      type: object
    FreepikTaskResponse:
      properties:
        data:
          $ref: '#/components/schemas/FreepikTaskData'
      required:
        - data
      type: object
    FreepikErrorResponse:
      properties:
        error:
          type: string
        message:
          type: string
      type: object
    FreepikTaskData:
      properties:
        generated:
          description: URLs to the generated images.
          items:
            format: uri
            type: string
          type: array
        status:
          enum:
            - CREATED
            - IN_PROGRESS
            - COMPLETED
            - FAILED
          type: string
        task_id:
          example: 046b6c7f-0b8a-43b9-b35d-6489e6daee91
          format: uuid
          type: string
      type: object
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````