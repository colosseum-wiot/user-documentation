Colosseum GPU Nodes Announcement
================================

In Spring 2023, we introduced the additional possibility to reserve GPU resources in a dedicated Colosseum cluster sponsored by the MassTech AI JumpStart program.

Users can now choose between 22 GPUs nodes hosted on the following servers:

* 2x NVIDIA DGX A100 – 8 NVIDIA `A100 <https://www.nvidia.com/en-us/data-center/a100/>`_ 40GB each.
* 1x Large Memory Node (LMN) - 6 NVIDIA V100 32GB and 3TB of RAM.

These GPUs will greatly enhance the computational power capabilities of an experiment, and, for example, will allow users to build and train AI/ML models easily.

Compared to an SRN reservation which is based on LXC, the GPUs are leveraged through Docker.

The reservation pages have been adjusted to allow this new feature.

A dedicated webpage (https://experiments.colosseum.net/images) has been created to manage Colosseum Docker images, and where users can interact with the Colosseum Docker registry via push, commit, export, and delete. (Reference :doc:`this page </container_mgmt/manage_docker_containers>`).

Base images have been already loaded for all teams, and users can build their own images via Dockerfiles by starting from this GitHub Repo: https://github.com/colosseum-wiot/colosseum-dockerfiles/.

A user can choose to reserve SRN and GPU separately, or together in a single reservation. Once a GPU reservation is up, users can simply ssh into the Docker container as for the SRN one. (Reference :doc:`this page </getting_started/logging_into_a_gpu>`). Moreover, to allow communication between LXC and Docker containers, users should follow :doc:`this guide </reservations/connecting_srn_and_gpu_reservations>`. Please, let us know any questions or issues that you might encounter.
