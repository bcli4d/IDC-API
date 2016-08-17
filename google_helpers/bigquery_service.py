"""

Copyright 2015, Institute for Systems Biology

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from oauth2client.client import flow_from_clientsecrets, GoogleCredentials
from googleapiclient import discovery
from oauth2client.file import Storage
from oauth2client import tools
from django.conf import settings
import httplib2

BIGQUERY_SCOPES = ['https://www.googleapis.com/auth/bigquery']


def get_bigquery_service():

    credentials = GoogleCredentials.from_stream(settings.GOOGLE_APPLICATION_CREDENTIALS).create_scoped(BIGQUERY_SCOPES)
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = discovery.build('bigquery', 'v2', http=http)

    return service
