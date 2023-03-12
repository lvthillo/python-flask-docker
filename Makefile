DOCKER_USERNAME ?= tansan78
APPLICATION_NAME ?= abctools
GIT_HASH ?= $(shell git log --format="%h" -n 1)

GCP_PROJECT ?= sanbeacon-1161
GCP_ARTIFACT_REG_HOST ?= us-west1-docker.pkg.dev
GCP_ARTIFACT_REG_DIR ?= abctools

all:
    $(info ==============================)


venv/bin/activate: requirements.txt
	python3	-m venv venv
	./venv/bin/pip install -r requirements.txt

# run all tests
# to run single tests: ./venv/bin/python3 -m unittest -v test.test_abc.TestABC_Py
test: venv/bin/activate
	./venv/bin/python3 -m test -j0

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete


gcloud_auth:
	gcloud auth configure-docker ${GCP_ARTIFACT_REG_HOST}

build: gcloud_auth
	docker build --tag ${GCP_ARTIFACT_REG_HOST}/${GCP_PROJECT}/${GCP_ARTIFACT_REG_DIR}/${APPLICATION_NAME}:${GIT_HASH} .

push: gcloud_auth
	docker push ${GCP_ARTIFACT_REG_HOST}/${GCP_PROJECT}/${GCP_ARTIFACT_REG_DIR}/${APPLICATION_NAME}:${GIT_HASH}

release: gcloud_auth
	docker pull ${GCP_ARTIFACT_REG_HOST}/${GCP_PROJECT}/${GCP_ARTIFACT_REG_DIR}/${APPLICATION_NAME}:${GIT_HASH}
	docker tag  ${GCP_ARTIFACT_REG_HOST}/${GCP_PROJECT}/${GCP_ARTIFACT_REG_DIR}/${APPLICATION_NAME}:${GIT_HASH} \
		   ${GCP_ARTIFACT_REG_HOST}/${GCP_PROJECT}/${GCP_ARTIFACT_REG_DIR}/${APPLICATION_NAME}:latest
	docker push ${GCP_ARTIFACT_REG_HOST}/${GCP_PROJECT}/${GCP_ARTIFACT_REG_DIR}/${APPLICATION_NAME}:latest


.PHONY: all test clean build
