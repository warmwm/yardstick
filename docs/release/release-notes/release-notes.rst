License
=======

OPNFV Euphrates release note for Yardstick Docs
are licensed under a Creative Commons Attribution 4.0 International License.
You should have received a copy of the license along with this.
If not, see <http://creativecommons.org/licenses/by/4.0/>.

The *Yardstick framework*, the *Yardstick test cases* are open-source software,
 licensed under the terms of the Apache License, Version 2.0.

OPNFV Euphrates Release Note for Yardstick
==========================================

.. toctree::
   :maxdepth: 2

.. _Yardstick: https://wiki.opnfv.org/yardstick

.. _Dashboard: http://testresults.opnfv.org/grafana/dashboard/db/yardstick-main

.. _NFV-TST001: http://www.etsi.org/deliver/etsi_gs/NFV-TST/001_099/001/01.01.01_60/gs_NFV-TST001v010101p.pdf


Abstract
--------

This document describes the release note of Yardstick project.


Version History
---------------
+-------------------+-----------+---------------------------------+
| *Date*            | *Version* | *Comment*                       |
|                   |           |                                 |
+-------------------+-----------+---------------------------------+
| December 15, 2017 | 5.1.0     | Yardstick for Euphrates release |
|                   |           |                                 |
+-------------------+-----------+---------------------------------+
| October 20, 2017  | 5.0.0     | Yardstick for Euphrates release |
|                   |           |                                 |
+-------------------+-----------+---------------------------------+


Important Notes
---------------

The software delivered in the OPNFV Yardstick_ Project, comprising the
*Yardstick framework*, the *Yardstick test cases* and the experimental
framework *Apex Lake* is a realization of the methodology in ETSI-ISG
NFV-TST001_.

The *Yardstick* framework is *installer*, *infrastructure* and *application*
independent.

OPNFV Euphrates Release
-----------------------

This Euphrates release provides *Yardstick* as a framework for NFVI testing
and OPNFV feature testing, automated in the OPNFV CI pipeline, including:

* Documentation generated with Sphinx

  * User Guide

  * Developer Guide

  * Release notes (this document)

  * Results

* Automated Yardstick test suite (daily, weekly)

  * Jenkins Jobs for OPNFV community labs

* Automated Yardstick test results visualization

  * Dashboard_ using Grafana (user:opnfv/password: opnfv), influxDB is used as
    backend

* Yardstick framework source code

* Yardstick test cases yaml files

* Yardstick plug-in configuration yaml files, plug-in install/remove scripts

For Euphrates release, the *Yardstick framework* is used for the following
testing:

* OPNFV platform testing - generic test cases to measure the categories:

  * Compute

  * Network

  * Storage

* OPNFV platform network service benchmarking(NSB)

  * NSB

* Test cases for the following OPNFV Projects:

  * Container4NFV

  * High Availability

  * IPv6

  * KVM

  * Parser

  * StorPerf

  * VSperf

  * virtual Traffic Classifier

The *Yardstick framework* is developed in the OPNFV community, by the
Yardstick_ team.

.. note:: The test case description template used for the Yardstick test cases
  is based on the document ETSI-ISG NFV-TST001_; the results report template
  used for the Yardstick results is based on the IEEE Std 829-2008.


Release Data
------------

+--------------------------------+-----------------------+
| **Project**                    | Yardstick             |
|                                |                       |
+--------------------------------+-----------------------+
| **Repo/tag**                   | yardstick/opnfv-5.1.0 |
|                                |                       |
+--------------------------------+-----------------------+
| **Yardstick Docker image tag** | opnfv-5.1.0           |
|                                |                       |
+--------------------------------+-----------------------+
| **Release designation**        | Euphrates             |
|                                |                       |
+--------------------------------+-----------------------+
| **Release date**               | December 15, 2017     |
|                                |                       |
+--------------------------------+-----------------------+
| **Purpose of the delivery**    | OPNFV Euphrates 5.1.0 |
|                                |                       |
+--------------------------------+-----------------------+


Deliverables
------------

Documents
^^^^^^^^^

 - User Guide: http://docs.opnfv.org/en/stable-euphrates/submodules/yardstick/docs/testing/user/userguide/index.html

 - Developer Guide: http://docs.opnfv.org/en/stable-euphrates/submodules/yardstick/docs/testing/developer/devguide/index.html


Software Deliverables
^^^^^^^^^^^^^^^^^^^^^


 - The Yardstick Docker image: https://hub.docker.com/r/opnfv/yardstick (tag: opnfv-5.1.0)


New Contexts
############

+--------------+-------------------------------------------+
| **Context**  | **Description**                           |
|              |                                           |
+--------------+-------------------------------------------+
| *Heat*       | Models orchestration using OpenStack Heat |
|              |                                           |
+--------------+-------------------------------------------+
| *Node*       | Models Baremetal, Controller, Compute     |
|              |                                           |
+--------------+-------------------------------------------+
| *Standalone* | Models VM running on Non-Managed NFVi     |
|              |                                           |
+--------------+-------------------------------------------+
| *Kubernetes* | Models VM running on Non-Managed NFVi     |
|              |                                           |
+--------------+-------------------------------------------+


New Runners
###########

+--------------+-------------------------------------------------------+
| **Runner**   | **Description**                                       |
|              |                                                       |
+--------------+-------------------------------------------------------+
| *Arithmetic* | Steps every run arithmetically according to specified |
|              | input value                                           |
|              |                                                       |
+--------------+-------------------------------------------------------+
| *Duration*   | Runs for a specified period of time                   |
|              |                                                       |
+--------------+-------------------------------------------------------+
| *Iteration*  | Runs for a specified number of iterations             |
|              |                                                       |
+--------------+-------------------------------------------------------+
| *Sequence*   | Selects input value to a scenario from an input file  |
|              | and runs all entries sequentially                     |
|              |                                                       |
+--------------+-------------------------------------------------------+


New Scenarios
#############

+----------------+-----------------------------------------------------+
| **Category**   | **Delivered**                                       |
|                |                                                     |
+----------------+-----------------------------------------------------+
| *Availability* | Attacker:                                           |
|                |                                                     |
|                | * baremetal, process                                |
|                |                                                     |
|                | HA tools:                                           |
|                |                                                     |
|                | * check host, openstack, process, service           |
|                | * kill process                                      |
|                | * start/stop service                                |
|                |                                                     |
|                | Monitor:                                            |
|                |                                                     |
|                | * command, process                                  |
|                |                                                     |
+----------------+-----------------------------------------------------+
| *Compute*      | * cpuload                                           |
|                |                                                     |
|                | * cyclictest                                        |
|                |                                                     |
|                | * lmbench                                           |
|                |                                                     |
|                | * lmbench_cache                                     |
|                |                                                     |
|                | * perf                                              |
|                |                                                     |
|                | * unixbench                                         |
|                |                                                     |
|                | * ramspeed                                          |
|                |                                                     |
|                | * cachestat                                         |
|                |                                                     |
|                | * memeoryload                                       |
|                |                                                     |
|                | * computecapacity                                   |
|                |                                                     |
|                | * SpecCPU2006                                       |
|                |                                                     |
+----------------+-----------------------------------------------------+
| *Networking*   | * iperf3                                            |
|                |                                                     |
|                | * netperf                                           |
|                |                                                     |
|                | * netperf_node                                      |
|                |                                                     |
|                | * ping                                              |
|                |                                                     |
|                | * ping6                                             |
|                |                                                     |
|                | * pktgen                                            |
|                |                                                     |
|                | * sfc                                               |
|                |                                                     |
|                | * sfc with tacker                                   |
|                |                                                     |
|                | * vtc instantion validation                         |
|                |                                                     |
|                | * vtc instantion validation with noisy neighbors    |
|                |                                                     |
|                | * vtc throughput                                    |
|                |                                                     |
|                | * vtc throughput in the presence of noisy neighbors |
|                |                                                     |
|                | * networkcapacity                                   |
|                |                                                     |
|                | * netutilization                                    |
|                |                                                     |
|                | * nstat                                             |
|                |                                                     |
|                | * pktgenDPDK                                        |
|                |                                                     |
+----------------+-----------------------------------------------------+
| *Parser*       | Tosca2Heat                                          |
|                |                                                     |
+----------------+-----------------------------------------------------+
| *Storage*      | fio                                                 |
|                |                                                     |
|                | bonnie++                                            |
|                |                                                     |
|                | storagecapacity                                     |
|                |                                                     |
+----------------+-----------------------------------------------------+
| *StorPerf*     | storperf                                            |
|                |                                                     |
+----------------+-----------------------------------------------------+
| *NSB*          | vPE thoughput test case                             |
|                |                                                     |
+----------------+-----------------------------------------------------+



New Test cases
^^^^^^^^^^^^^^

* Generic NFVI test cases

 * OPNFV_YARDSTICK_TCO78 - SPEC CPU 2006

 * OPNFV_YARDSTICK_TCO79 - Bonnie++

* Kubernetes Test cases

 * OPNFV_YARDSTICK_TCO80 - NETWORK LATENCY BETWEEN CONTAINER

 * OPNFV_YARDSTICK_TCO81 - NETWORK LATENCY BETWEEN CONTAINER AND VM


Version Change
--------------

Module Version Changes
^^^^^^^^^^^^^^^^^^^^^^

This is the fifth tracked release of Yardstick. It is based on following
upstream versions:

- OpenStack Ocata

- OpenDayLight Nitrogen

- ONOS Junco


Document Version Changes
^^^^^^^^^^^^^^^^^^^^^^^^

This is the fifth tracked version of the Yardstick framework in OPNFV.
It includes the following documentation updates:

- Yardstick User Guide: add "network service benchmarking(NSB)" chapter;
  add "Yardstick - NSB Testing -Installation" chapter; add "Yardstick API" chapter;
  add "Yardstick user interface" chapter; Update Yardstick installation chapter;

- Yardstick Developer Guide

- Yardstick Release Notes for Yardstick: this document


Feature additions
^^^^^^^^^^^^^^^^^

- Yardstick RESTful API support

- Network service benchmarking

- Stress testing with Bottlenecks team

- Yardstick framework improvement:

  - yardstick report CLI

  - Node context support OpenStack configuration via Ansible

  - Https support

  - Kubernetes context type

- Yardstick container local GUI

- Python 3 support


Scenario Matrix
---------------

For Euphrates 5.0.0, Yardstick was tested on the following scenarios:

+--------------------------+------+---------+------+------+
| Scenario                 | Apex | Compass | Fuel | Joid |
+==========================+======+=========+======+======+
| os-nosdn-nofeature-noha  |      |         | X    | X    |
+--------------------------+------+---------+------+------+
| os-nosdn-nofeature-ha    | X    | X       | X    | X    |
+--------------------------+------+---------+------+------+
| os-odl_l2-nofeature-ha   |      | X       | X    | X    |
+--------------------------+------+---------+------+------+
| os-odl_l2-nofeature-noha |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-odl_l3-nofeature-ha   | X    | X       | X    |      |
+--------------------------+------+---------+------+------+
| os-odl_l3-nofeature-noha |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-onos-sfc-ha           |      |         |      |      |
+--------------------------+------+---------+------+------+
| os-onos-nofeature-ha     |      | X       |      | X    |
+--------------------------+------+---------+------+------+
| os-onos-nofeature-noha   |      |         |      |      |
+--------------------------+------+---------+------+------+
| os-odl_l2-sfc-ha         |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-odl_l2-sfc-noha       |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-odl_l2-bgpvpn-ha      | X    |         | X    |      |
+--------------------------+------+---------+------+------+
| os-odl_l2-bgpvpn-noha    |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-nosdn-kvm-ha          | X    |         | X    |      |
+--------------------------+------+---------+------+------+
| os-nosdn-kvm-noha        |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-nosdn-ovs-ha          |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-nosdn-ovs-noha        |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-ocl-nofeature-ha      |      | X       |      |      |
+--------------------------+------+---------+------+------+
| os-nosdn-lxd-ha          |      |         |      | X    |
+--------------------------+------+---------+------+------+
| os-nosdn-lxd-noha        |      |         |      | X    |
+--------------------------+------+---------+------+------+
| os-nosdn-fdio-ha         | X    |         |      |      |
+--------------------------+------+---------+------+------+
| os-odl_l2-fdio-noha      | X    |         |      |      |
+--------------------------+------+---------+------+------+
| os-odl-gluon-noha        | X    |         |      |      |
+--------------------------+------+---------+------+------+
| os-nosdn-openo-ha        |      | X       |      |      |
+--------------------------+------+---------+------+------+
| os-nosdn-kvm_ovs_dpdk    |      |         | X    |      |
| -noha                    |      |         |      |      |
+--------------------------+------+---------+------+------+
| os-nosdn-kvm_ovs_dpdk-ha |      |         | X    |      |
+--------------------------+------+---------+------+------+
| os-nosdn-kvm_ovs_dpdk    |      |         | X    |      |
| _bar-ha                  |      |         |      |      |
+--------------------------+------+---------+------+------+
| os-nosdn-kvm_ovs_dpdk    |      |         | X    |      |
| _bar-noha                |      |         |      |      |
+--------------------------+------+---------+------+------+
| opnfv_os-ovn-nofeature-  | X    |         |      |      |
| noha_daily               |      |         |      |      |
+--------------------------+------+---------+------+------+

Test results
------------

Test results are available in:

 - jenkins logs on CI: https://build.opnfv.org/ci/view/yardstick/

The reporting pages can be found at:

+---------------+-------------------------------------------------------------------------------------+
| apex          | http://testresults.opnfv.org/reporting/euphrates/yardstick/status-apex.html         |
+---------------+-------------------------------------------------------------------------------------+
| compass       | http://testresults.opnfv.org/reporting/euphrates/yardstick/status-compass.html      |
+---------------+-------------------------------------------------------------------------------------+
| fuel\@x86     | http://testresults.opnfv.org/reporting/euphrates/yardstick/status-fuel@x86.html     |
+---------------+-------------------------------------------------------------------------------------+
| fuel\@aarch64 | http://testresults.opnfv.org/reporting/euphrates/yardstick/status-fuel@aarch64.html |
+---------------+-------------------------------------------------------------------------------------+
| joid          | http://testresults.opnfv.org/reporting/euphrates/yardstick/status-joid.html         |
+---------------+-------------------------------------------------------------------------------------+

Known Issues/Faults
^^^^^^^^^^^^^^^^^^^


Corrected Faults
^^^^^^^^^^^^^^^^

Euphrates 5.1.0:

+---------------------+-------------------------------------------------------------------------+
| **JIRA REFERENCE**  | **DESCRIPTION**                                                         |
|                     |                                                                         |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-841 | Fix various NSB license issues                                          |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-73  | How To Work with Test Cases                                             |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-500 | VNF testing documentation                                               |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-826 | Allow overriding Heat IP addresses to match traffic generator profile   |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-828 | Refactor doc/testing/user/userguide "Yardstick Installation"            |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-830 | build_yardstick_image Ansible mount module doesn't work on Ubuntu 14.04 |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-833 | ansible_common transform password into lower case                       |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-847 | tc006, tc079, tc082 miss grafana dashboard in local deployment          |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-849 | kill process do not accurately kill the process like "nova-api"         |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-850 | tc023 miss description and tc050-58 wrong description                   |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-852 | tc078 cpu2006 fails in some situation                                   |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-854 | yardstick docker lack of trex_client                                    |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-867 | testcase tc078 have no data stored or dashboard to show results         |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-871 | Remove img_modify_playbook assignation in build_yardstick_image.yml     |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-829 | "nsb_setup.sh" doesn't parse the controller IP correctly                |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-839 | NSB Prox BM test cases to be fixed for incorporating scale-up           |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-840 | NSB Prox test documentation of vPE and LW-AFTR test cases               |
+---------------------+-------------------------------------------------------------------------+
| JIRA: YARDSTICK-848 | NSB "Prox" : Cleanup duplicated traffic profile                         |
+---------------------+-------------------------------------------------------------------------+




Euphrates 5.0.0:

+---------------------+--------------------------------------------+
| **JIRA REFERENCE**  | **DESCRIPTION**                            |
|                     |                                            |
+---------------------+--------------------------------------------+
| JIRA: YARDSTICK-599 | Could not load EntryPoint.parse when using |
|                     | 'openstack -h'                             |
+---------------------+--------------------------------------------+
| JIRA: YARDSTICK-602 | Don't rely on staic ip addresses as they   |
|                     | are dynamic                                |
+---------------------+--------------------------------------------+


Euphratess 5.0.0 known restrictions/issues
------------------------------------------
+-----------+-----------+----------------------------------------------+
| Installer | Scenario  | Issue                                        |
+===========+===========+==============================================+
| any       | \*-bgpvpn | Floating ips not supported. Some Test cases  |
|           |           | related to floating ips are excluded.        |
+-----------+-----------+----------------------------------------------+
| any       | odl_l3-\* | Some test cases related to using floating IP |
|           |           | addresses fail because of a known ODL bug.   |
|           |           |                                              |
+-----------+-----------+----------------------------------------------+
| compass   | odl_l2-\* | In some test cases, VM instance will failed  |
|           |           | raising network interfaces.                  |
|           |           |                                              |
+-----------+-----------+----------------------------------------------+


Useful links
------------

 - wiki project page: https://wiki.opnfv.org/display/yardstick/Yardstick

 - wiki Yardstick Euphrates release planing page: https://wiki.opnfv.org/display/yardstick/Yardstick+Euphrates+Release+Planning

 - Yardstick repo: https://git.opnfv.org/cgit/yardstick

 - Yardstick CI dashboard: https://build.opnfv.org/ci/view/yardstick

 - Yardstick grafana dashboard: http://testresults.opnfv.org/grafana/

 - Yardstick IRC chanel: #opnfv-yardstick
