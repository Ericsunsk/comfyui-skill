> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Relight an image

> Relight an image using AI. This endpoint accepts a variety of parameters to customize the generated images.




## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/freepik/v1/ai/image-relight
openapi: 3.0.2
info:
  title: Comfy API
  version: '1.0'
servers:
  - url: https://api.comfy.org
security: []
paths:
  /proxy/freepik/v1/ai/image-relight:
    post:
      tags:
        - Freepik
        - Proxy
      summary: Relight an image
      description: >
        Relight an image using AI. This endpoint accepts a variety of parameters
        to customize the generated images.
      operationId: FreepikMagnificRelight
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FreepikMagnificRelightRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FreepikTaskResponse'
          description: OK - The relight process has started
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
    FreepikMagnificRelightRequest:
      properties:
        advanced_settings:
          properties:
            blacks:
              default: 50
              description: Adjust the level of black color in the image.
              maximum: 100
              minimum: 0
              type: integer
            brightness:
              default: 50
              description: Adjust the level of brightness in the image.
              maximum: 100
              minimum: 0
              type: integer
            contrast:
              default: 50
              description: Adjust the level of contrast in the image.
              maximum: 100
              minimum: 0
              type: integer
            engine:
              default: automatic
              description: |
                Engine preset for relighting:
                - balanced: Well-rounded, general-purpose option
                - cool: Brighter with cooler tones
                - real: Aims to enhance photographic quality (Experimental)
                - illusio: Optimized for illustrations and drawings
                - fairy: Suited for fantasy-themed images
                - colorful_anime: Ideal for anime, cartoons, and vibrant colors
                - hard_transform: Significantly alters the original image
                - softy: Slightly softer effect, suitable for graphic designs
              enum:
                - automatic
                - balanced
                - cool
                - real
                - illusio
                - fairy
                - colorful_anime
                - hard_transform
                - softy
              type: string
            fixed_generation:
              default: false
              description: >-
                When enabled, using the same settings will consistently produce
                the same image.
              type: boolean
            saturation:
              default: 50
              description: Adjust the level of saturation in the image.
              maximum: 100
              minimum: 0
              type: integer
            transfer_light_a:
              default: automatic
              description: Adjusts the intensity of light transfer.
              enum:
                - automatic
                - low
                - medium
                - normal
                - high
                - high_on_faces
              type: string
            transfer_light_b:
              default: automatic
              description: >-
                Also modifies light transfer intensity. Can be combined with
                transfer_light_a for varied effects.
              enum:
                - automatic
                - composition
                - straight
                - smooth_in
                - smooth_out
                - smooth_both
                - reverse_both
                - soft_in
                - soft_out
                - soft_mid
                - strong_mid
                - style_shift
                - strong_shift
              type: string
            whites:
              default: 50
              description: Adjust the level of white color in the image.
              maximum: 100
              minimum: 0
              type: integer
          type: object
        change_background:
          default: true
          description: >-
            When enabled, changes the background based on prompt and/or
            reference image. Useful for product placement and portraits.
          type: boolean
        image:
          description: Base64 or URL of the image to do the relight
          type: string
        interpolate_from_original:
          default: false
          description: >-
            When enabled, makes the final image interpolate from the original
            using the light transfer strength slider.
          type: boolean
        light_transfer_strength:
          default: 100
          description: >-
            Level of light transfer intensity. 0% keeps closest to original,
            100% is maximum transfer.
          maximum: 100
          minimum: 0
          type: integer
        preserve_details:
          default: true
          description: >-
            Maintains texture and small details of the original image. Good for
            product photography, texts, etc.
          type: boolean
        prompt:
          description: >
            You can guide the generation process and influence the light
            transfer with a descriptive prompt.

            IMPORTANT: You can emphasize specific aspects of the light in your
            prompt by using a number in parentheses, ranging from 1 to 1.4, like
            "(dark scene:1.3)".
          type: string
        style:
          default: standard
          description: Style preset for the relight operation.
          enum:
            - standard
            - darker_but_realistic
            - clean
            - smooth
            - brighter
            - contrasted_n_hdr
            - just_composition
          type: string
        transfer_light_from_lightmap:
          description: >-
            Base64 or URL of the lightmap for light transfer. Incompatible with
            'transfer_light_from_reference_image'
          type: string
        transfer_light_from_reference_image:
          description: >-
            Base64 or URL of the reference image for light transfer.
            Incompatible with 'transfer_light_from_lightmap'
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