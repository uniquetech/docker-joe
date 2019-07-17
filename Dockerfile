FROM jlesage/baseimage-gui:alpine-3.9-glibc-v3.5.2

LABEL name="jobscheduler-joe"

ARG JOE_VERSION
ENV SOS_SOURCE_URL='https://download.sos-berlin.com/JobScheduler' \
	JOE_VERSION=${JOE_VERSION:-'1.12.9'}

WORKDIR /tmp

RUN apk add --update --no-cache openjdk8-jre \
	curl \
	xmlstarlet \
	gtk+2.0 \
	&& curl --progress "${SOS_SOURCE_URL}.${JOE_VERSION%.*}/jobscheduler_linux-x64_joe.${JOE_VERSION}.tar.gz" | tar -xvz \
	&& xmlstarlet ed --inplace -u "/AutomatedInstallation/com.izforge.izpack.panels.TargetPanel/installpath" --value "/opt/sos-berlin.com/joe" \
		-u "/AutomatedInstallation/com.izforge.izpack.panels.UserPathPanel/UserPathPanelElement" --value "/opt/sos-berlin.com/joe" /tmp/jobscheduler_joe.${JOE_VERSION}/joe_install.xml \
	&& /tmp/jobscheduler_joe.${JOE_VERSION}/setup.sh /tmp/jobscheduler_joe.${JOE_VERSION}/joe_install.xml \
	&& rm -rf /tmp/jobscheduler_joe.${JOE_VERSION}

# Command to run the jobscheduler object editor

CMD /opt/sos-berlin.com/joe/bin/jobeditor.sh
