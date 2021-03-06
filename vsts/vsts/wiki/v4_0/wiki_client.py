# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...vss_client import VssClient
from . import models


class WikiClient(VssClient):
    """Wiki
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(WikiClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'bf7d82a0-8aa5-4613-94ef-6172a5ea01f3'

    def get_pages(self, project, wiki_id, path=None, recursion_level=None, version_descriptor=None):
        """GetPages.
        [Preview API] Gets metadata or content of the wiki pages under the provided page path.
        :param str project: Project ID or project name
        :param str wiki_id: ID of the wiki from which the page is to be retrieved.
        :param str path: Path from which the pages are to retrieved.
        :param str recursion_level: Recursion level for the page retrieval. Defaults to None (Optional).
        :param :class:`<GitVersionDescriptor> <wiki.v4_0.models.GitVersionDescriptor>` version_descriptor: Version descriptor for the page. Defaults to default branch (Optional).
        :rtype: [WikiPage]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_id is not None:
            route_values['wikiId'] = self._serialize.url('wiki_id', wiki_id, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.VersionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.Version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.VersionOptions'] = version_descriptor.version_options
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='4.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[WikiPage]', response)

    def get_page_text(self, project, wiki_id, path=None, recursion_level=None, version_descriptor=None):
        """GetPageText.
        [Preview API] Gets metadata or content of the wiki pages under the provided page path.
        :param str project: Project ID or project name
        :param str wiki_id: ID of the wiki from which the page is to be retrieved.
        :param str path: Path from which the pages are to retrieved.
        :param str recursion_level: Recursion level for the page retrieval. Defaults to None (Optional).
        :param :class:`<GitVersionDescriptor> <wiki.v4_0.models.GitVersionDescriptor>` version_descriptor: Version descriptor for the page. Defaults to default branch (Optional).
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_id is not None:
            route_values['wikiId'] = self._serialize.url('wiki_id', wiki_id, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.VersionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.Version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.VersionOptions'] = version_descriptor.version_options
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='4.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_page_zip(self, project, wiki_id, path=None, recursion_level=None, version_descriptor=None):
        """GetPageZip.
        [Preview API] Gets metadata or content of the wiki pages under the provided page path.
        :param str project: Project ID or project name
        :param str wiki_id: ID of the wiki from which the page is to be retrieved.
        :param str path: Path from which the pages are to retrieved.
        :param str recursion_level: Recursion level for the page retrieval. Defaults to None (Optional).
        :param :class:`<GitVersionDescriptor> <wiki.v4_0.models.GitVersionDescriptor>` version_descriptor: Version descriptor for the page. Defaults to default branch (Optional).
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_id is not None:
            route_values['wikiId'] = self._serialize.url('wiki_id', wiki_id, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.VersionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.Version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.VersionOptions'] = version_descriptor.version_options
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='4.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def create_update(self, update, project, wiki_id, version_descriptor=None):
        """CreateUpdate.
        [Preview API] Use this API to create, edit, delete and reorder a wiki page and also to add attachments to a wiki page. For every successful wiki update creation a Git push is made to the backing Git repository. The data corresponding to that Git push is added in the response of this API.
        :param :class:`<WikiUpdate> <wiki.v4_0.models.WikiUpdate>` update:
        :param str project: Project ID or project name
        :param str wiki_id: ID of the wiki in which the update is to be made.
        :param :class:`<GitVersionDescriptor> <wiki.v4_0.models.GitVersionDescriptor>` version_descriptor: Version descriptor for the version on which the update is to be made. Defaults to default branch (Optional).
        :rtype: :class:`<WikiUpdate> <wiki.v4_0.models.WikiUpdate>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_id is not None:
            route_values['wikiId'] = self._serialize.url('wiki_id', wiki_id, 'str')
        query_parameters = {}
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.VersionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.Version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.VersionOptions'] = version_descriptor.version_options
        content = self._serialize.body(update, 'WikiUpdate')
        response = self._send(http_method='POST',
                              location_id='d015d701-8038-4e7b-8623-3d5ca6813a6c',
                              version='4.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('WikiUpdate', response)

    def create_wiki(self, wiki_to_create, project=None):
        """CreateWiki.
        [Preview API] Creates a backing git repository and does the intialization of the wiki for the given project.
        :param :class:`<GitRepository> <wiki.v4_0.models.GitRepository>` wiki_to_create: Object containing name of the wiki to be created and the ID of the project in which the wiki is to be created. The provided name will also be used in the name of the backing git repository. If this is empty, the name will be auto generated.
        :param str project: Project ID or project name
        :rtype: :class:`<WikiRepository> <wiki.v4_0.models.WikiRepository>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(wiki_to_create, 'GitRepository')
        response = self._send(http_method='POST',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='4.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiRepository', response)

    def get_wikis(self, project=None):
        """GetWikis.
        [Preview API] Retrieves wiki repositories in a project or collection.
        :param str project: Project ID or project name
        :rtype: [WikiRepository]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='4.0-preview.1',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[WikiRepository]', response)

