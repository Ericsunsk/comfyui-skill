> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Style transfer an image

> Style transfer an image using AI.



## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/freepik/v1/ai/image-style-transfer
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/freepik/v1/ai/image-style-transfer:
    post:
      tags:
        - Freepik
        - Proxy
      summary: Style transfer an image
      description: Style transfer an image using AI.
      operationId: FreepikMagnificStyleTransfer
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FreepikMagnificStyleTransferRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikTaskData'
          description: OK - The style transfer process has started
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
    FreepikMagnificStyleTransferRequest:
      properties:
        engine:
          default: balanced
          description: Engine preset for style transfer
          enum:
            - balanced
            - definio
            - illusio
            - 3d_cartoon
            - colorful_anime
            - caricature
            - real
            - super_real
            - softy
          type: string
        fixed_generation:
          default: false
          description: >-
            When enabled, using the same settings will consistently produce the
            same image.
          type: boolean
        flavor:
          default: faithful
          description: Flavor of the transferring style
          enum:
            - faithful
            - gen_z
            - psychedelia
            - detaily
            - clear
            - donotstyle
            - donotstyle_sharp
          type: string
        image:
          description: Base64 or URL of the image to do the style transfer
          type: string
        is_portrait:
          default: false
          description: Indicates whether the image should be processed as a portrait.
          type: boolean
        portrait_beautifier:
          description: >-
            Facial beautification on portrait images. Only used if is_portrait
            is true.
          enum:
            - beautify_face
            - beautify_face_max
          type: string
        portrait_style:
          default: standard
          description: >-
            Visual style applied to portrait images. Only used if is_portrait is
            true.
          enum:
            - standard
            - pop
            - super_pop
          type: string
        prompt:
          description: Prompt for the AI model
          type: string
        reference_image:
          description: Base64 or URL of the reference image for style transfer
          type: string
        structure_strength:
          default: 50
          description: Allows to maintain the structure of the original image
          maximum: 100
          minimum: 0
          type: integer
        style_strength:
          default: 100
          description: Percentage of style strength
          maximum: 100
          minimum: 0
          type: integer
        webhook_url:
          description: Optional callback URL for async notifications.
          example: https://www.example.com/webhook
          format: uri
          type: string
      required:
        - image
        - reference_image
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
    FreepikErrorResponse:
      properties:
        error:
          type: string
        message:
          type: string
      type: object
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````