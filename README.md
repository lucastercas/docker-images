# Docker Images

Since most of the programs I use I try to run on containers,
some of the images I found for these programs were
outdated/not good/proprietary. So I made this repository to
store the my own images.

I try to keep most of them updated with their upstreams, but
I haven't yet setup a pipeline to keep them updated with each update
to upstream.

## Current Images

1. CLI Programs
   1. [x] Helm
      1. [ ] Add documentation (what is helm, etc)
   2. [x] RKE
      1. [ ] Add documentation (what is rke, how to use the image, etc)
   3. [x] Kubectl
      1. [ ] Add documentation
2. Web
   1. [x] Jenkins
      1. [ ]
   2. [ ] Moodle
      1. [ ]
   3. [ ] PG Badger
      1. [ ] Finish image
      2. [ ] Add documentation
   4. [ ] otrs
      1. [ ] Finish image
      2. [ ] Add documentation

## To Do

1. CI/CD Pipeline
2. How to keep them up to date with upstream automatically?
   1. The idea is that, on pushes to relevant branches on the upstream
      of each of these images, a pipeline is run to build the image and
      push the new image to docker hub.
