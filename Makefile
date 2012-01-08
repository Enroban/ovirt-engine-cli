all: rpm

rpmrelease:=1
rpmversion=1.0
RPMTOP=$(shell bash -c "pwd -P")/rpmtop
SPEC=ovirt-engine-cli.spec

TARBALL=ovirt-engine-cli-$(rpmversion)-$(rpmrelease).tar.gz
SRPM=$(RPMTOP)/SRPMS/ovirt-engine-cli-$(rpmversion)-$(rpmrelease).src.rpm

TESTS=pyflakes

test: pyflakes exceptions
	echo $(rpmrelease) $(rpmversion)

pyflakes:
	@git ls-files '*.py' | xargs pyflakes \
	    || (echo "Pyflakes errors or pyflakes not found"; exit 1)

.PHONY: tarball
tarball: $(TARBALL)
$(TARBALL): Makefile #$(TESTS)
	tar zcf $(TARBALL) `git ls-files `

.PHONY: srpm rpm
srpm: $(SRPM)
$(SRPM): $(TARBALL) ovirt-engine-cli.spec.in
	sed 's/^Version:.*/Version: $(rpmversion)/;s/^Release:.*/Release: $(rpmrelease)/' ovirt-engine-cli.spec.in > $(SPEC)
	mkdir -p $(RPMTOP)/{RPMS,SRPMS,SOURCES,BUILD}
	rpmbuild -bs \
	    --define="_topdir $(RPMTOP)" \
	    --define="_sourcedir ." $(SPEC)

rpm: $(SRPM)
	rpmbuild --define="_topdir $(RPMTOP)" --rebuild $<

clean:
	$(RM) *~ *.pyc ovirt-engine-cli*.tar.gz $(SPEC)
	$(RM) -r rpmtop