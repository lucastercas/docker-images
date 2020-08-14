FROM debian:stable

ARG OTRS_VERSION=6.0.29

RUN apt-get -y update
RUN apt-get install -y --no-install-recommends \
  perl-modules \
  libarchive-zip-perl \
  libcrypt-eksblowfish-perl \
  libtimedate-perl \
  libdatetime-perl \
  libdbi-perl \
  libdbd-mysql-perl \
  libdbd-odbc-perl \
  libdbd-pg-perl \
  libencode-hanextra-perl \
  libio-socket-ssl-perl \
  libjson-xs-perl \
  libmail-imapclient-perl \
  libio-socket-ssl-perl \
  libauthen-sasl-perl \
  libauthen-ntlm-perl \
  libapache2-mod-perl2 \
  libmoo-perl \
  libnet-dns-perl \
  libnet-ldap-perl \
  libtemplate-perl \
  libtext-csv-xs-perl \
  libxml-libxml-perl \
  libxml-libxslt-perl \
  libxml-parser-perl \
  libyaml-libyaml-perl

WORKDIR /opt
# Download source, extract and move to default directory (/opt/otrs)
ADD http://ftp.otrs.org/pub/otrs/otrs-"${OTRS_VERSION}".tar.gz .
RUN tar xzf ./otrs-"${OTRS_VERSION}".tar.gz && \
  mv otrs-"${OTRS_VERSION}" ./otrs && \
  rm otrs-"${OTRS_VERSION}".tar.gz
# Check perl modules and create default user and group
RUN perl ./otrs/bin/otrs.CheckModules.pl && \
  useradd -d /opt/otrs -c 'OTRS user' otrs && \
  usermod -G www otrs && \
  cp /opt/otrs/Kernel/Config.pm.dist /opt/otrs/Kernel/Config.pm && \
  perl -cw /opt/otrs/bin/cgi-bin/index.pl && \
  perl -cw /opt/otrs/bin/cgi-bin/customer.pl && \
  perl -cw /opt/otrs/bin/otrs.Console.pl
EXPOSE 80
