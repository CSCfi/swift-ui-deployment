### .yml files for staging UI services on Openshift

### Usage
Apart from the internal database, the services `swift-x-account-sharing`,
`swift-sharing-request`, `swiftui-upload-runner` and `swift-browser-ui`
are deployed using images hosted on Docker Hub. The Docker Hub images for
staging builds are encouraged to use build numbering, since forcing
Openshift to re-pull the images using the same tag is a workaround instead of
a proper behavior.

#### internal database setup
Internal database is created with the Openshift default PostgreSQL image.
Both `swift-x-account-sharing` and `swift-sharing-request` require a
separate database when deployed on Openshift, so two database initializations
are needed.

`swift-x-account-sharing` database can be initialized with the script in
the file `sharing-database.sh`, by executing the contents of the script in
the pod terminal on Openshift.

`swift-sharing-request` database can be initialized with the script in
the file `request-database.sh`, by executing the contents of the script in
the pod terminal on Openshift.

#### swift-x-account-sharing staging setup
`swift-x-account-sharing` can be deployed with an image from Docker Hub, using
the file `sharing.yml`. The following environment variables need to be
specified in order for the image to function:

    - `SHARING_DB_HOST` for the database internal address / hostname
    - `SHARING_DB_PASSWORD` for the database password
    - `SWIFT_UI_API_AUTH_TOKENS` for the global API access tokens

#### swift-sharing-request staging setup
`swift-sharing-request` can be deployed with an image from Docker Hub, using
the file `request.yml`. The following environment variables need to be
specified in order for the image to function:

    - `REQUEST_DB_HOST` for the database internal address / hostname
    - `REQUEST_DB_PASSWORD` for the database password
    - `SWIFT_UI_API_AUTH_TOKENS` for the global API access tokens

#### swiftui-upload-runner staging setup
`swiftui-upload-runner` can be deployed with an image from Docker Hub, using
the file `upload.yml`. The following environment variables need to be
specified in order for the image to function:

    - `OS_AUTH_URL` for the Openstack authentication URL
    - `SWIFT_UI_API_AUTH_TOKENS` for the global API access tokens

#### swift-browser-ui staging
`swift-browser-ui` can be deployed with an image from Docker Hub, using the
file `ui.yml`. The following environment variables need to be specified in
order for the image to function:

    - `BROWSER_START_SHARING_ENDPOINT_URL` for the sharing API external URL
    - `BROWSER_START_REQUEST_ENDPOINT_URL` for the request API external URL
    - `BROWSER_START_AUTH_ENDPOINT_URL` for the Openstack authentication URL
    - `SWIFT_UI_SHARING_REQUEST_TOKEN` for the global API token used for
      accessing the sharing and request APIs
    - `BROWSER_START_RUNNER_ENDPOINT` for the internal address / hostname of
      the upload runner service
    - `BROWSER_START_RUNNER_EXT_ENDPOINT` for the external address of the
      upload runner service
    - `BROWSER_START_SHARING_INT_ENDPOINT_URL` for the internal address / 
      hostname of the sharing API
    - `BROWSER_START_REQUEST_INT_ENDPOINT_URL` for the internal address /
      hostname of the request API
    - `BROWSER_DEBUG` for enabling the debug logs for staging instance

#### Staging environment services
All services need to be present in order for the `swift-browser-ui` to work
as intended. The service descriptions can be foun from their respective YAML
files and can be imported from there.

#### Routes
The `swift-x-account-sharing`, `swift-sharing-request`, `swiftui-upload-runner`
and `swift-browser-ui` services require external routes to operate. These routes
are used for public facing operations. Setting up the routes is outside the
scope of this readme. The routes can be chosen at will, but the required ones
need to be transfered over to the `swift-browser-ui` environment variables so
they can be made discoverable.

#### Staging environment upgrade
The staging environment services can be uploaded by switching over to the
new build tag, by editing the service YAML on Openshift. The upgrade can
be forced to the currently used tag by scaling pod number to zero and forcing
the re-pull of the tag, but this is not the preferred way.
