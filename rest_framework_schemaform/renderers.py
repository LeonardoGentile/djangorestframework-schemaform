# -*- coding: utf-8 -*-
from rest_framework import renderers
from .serializers import JsonSchemaSerializer

import json


class JSONSchemaRenderer(renderers.JSONRenderer):
    media_type = 'application/schema+json'
    format = 'schema+json'
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # Look up the Django model
        renderer_context = renderer_context or {}
        view = renderer_context.get('view')
        response = renderer_context.get('response')
        queryset = view.get_queryset()
        model = queryset.model
        instance = model()
        # Pass the Django model to the serializer
        serializer = JsonSchemaSerializer(instance=instance)
        # Return the schema only if no errors occurred
        if response.exception:
            data = data
        else:
            data = None
        # Render the serializer result to json
        result = serializer.to_representation(data)

        return json.dumps(result)
