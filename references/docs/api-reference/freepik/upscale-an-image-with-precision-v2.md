> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Upscale an image with Precision V2

> Upscales an image while adding new visual elements or details (V2).
This endpoint may modify the original image content based on the prompt and inferred context.
Upon submission, it returns a unique task_id which can be used to track the progress.




## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/freepik/v1/ai/image-upscaler-precision-v2
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/freepik/v1/ai/image-upscaler-precision-v2:
    post:
      tags:
        - Freepik
        - Proxy
      summary: Upscale an image with Precision V2
      description: >
        Upscales an image while adding new visual elements or details (V2).

        This endpoint may modify the original image content based on the prompt
        and inferred context.

        Upon submission, it returns a unique task_id which can be used to track
        the progress.
      operationId: FreepikMagnificUpscalerPrecisionV2
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FreepikMagnificUpscalerPrecisionV2Request'
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
    FreepikMagnificUpscalerPrecisionV2Request:
      properties:
        flavor:
          description: |
            Image processing flavor:
            - sublime: Optimized for artistic and illustrated images
            - photo: Optimized for photographic images
            - photo_denoiser: Specialized for photos with noise reduction
          enum:
            - sublime
            - photo
            - photo_denoiser
          type: string
        image:
          description: |
            Source image to upscale. Accepts either:
            - A publicly accessible HTTPS URL pointing to the image
            - A base64-encoded image string
          type: string
        scale_factor:
          description: >-
            Image scaling factor. Determines how much larger the output will be
            compared to input.
          maximum: 16
          minimum: 2
          type: integer
        sharpen:
          default: 7
          description: >-
            Image sharpness intensity control. Higher values increase edge
            definition and clarity.
          maximum: 100
          minimum: 0
          type: integer
        smart_grain:
          default: 7
          description: >-
            Intelligent grain/texture enhancement. Higher values add more
            fine-grained texture.
          maximum: 100
          minimum: 0
          type: integer
        ultra_detail:
          default: 30
          description: >-
            Ultra detail enhancement level. Higher values create more intricate
            details.
          maximum: 100
          minimum: 0
          type: integer
        webhook_url:
          description: >-
            Optional callback URL that will receive asynchronous notifications
            when the upscaling task completes.
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