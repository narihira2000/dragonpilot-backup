![](https://i.imgur.com/b0ZyIx5.jpg)

Dragonpilot Backup
=======================
This repository tries to back up each version of Dragonpilot release3. You can switch to the brance you want to install specific version. All branches comes from forks by others, if you have any concern, do not use it.

Installation
------
Enter the url as the format below:
```
https://smiskol.com/fork/narihira2000/{branch}
```
You can replace the `{branch}` in the end of url by the version you want to install that version. For example, enter `https://smiskol.com/fork/narihira2000/r3-v2023.05.12` to install release3 v2023.05.12.

Backed up versions
------
* [x] v2023.07.05 - Backed up from me (Forked from Dragonpilot Official's repository).
* [x] v2023.05.12 - Backed up from [tranlocquy](https://github.com/tranlocquy/dragonpilot).
* [x] v2023.03.27 - Backed up from [Jimmyyk](https://github.com/Jimmyyk/dragonpilot/tree/release3).
* [x] v2023.02.18 - Backed up from [acornsites](https://github.com/acornsites/dragonpilot/tree/077dc8f7def2b98afe2bb66753b611b5fa0ee196).
* [x] v2023.02.15 - Backed up from [hankteng19650323](https://github.com/hankteng19650323/dragonpilot).
* [x] v2023.01.10 - Backed up from [umasuthan1304](https://github.com/umasuthan1304/dragonpilot).
* [x] v2022.12.13 - Backed up from [stlnick3](https://github.com/stlnick3/openpilot/tree/release3).
* [x] v2022.11.14 - Backed up from [loveloveses](https://github.com/loveloveses/dragonpilot).
* [x] v2022.11.01 - Backed up from [millsdmb](https://github.com/millsdmb/dragonpilot).
* [x] v2022.09.20 - Backed up from [sunnyc-op](https://github.com/sunnyc-op/dragonpilot).
* [x] v2022.09.12 - Backed up from [ramazansancar](https://github.com/ramazansancar/dragonpilot/tree/b064f7ea3b09dc0e431c50ea11a5b919286e583c).
* [x] v2022.09.04 - Backed up from [modal0809](https://github.com/modal0809/openpilot/tree/release3).
* [x] v2022.08.14 - Backed up from [tuna32416](https://github.com/tuna32416/openpilot/tree/release3).
* [x] v2022.07.29 - Backed up from [TheCrowd](https://github.com/TheCrowd/dragonpilot).
* [x] v2022.07.01 - Backed up from [aaronzandman](https://github.com/aaronzandman/openpilot).
* [x] v2022.06.16 - Backed up from [UhnTiss](https://github.com/UhnTiss/openpilot).

Missing versions
------
* [ ] v2023.07.04
* [ ] v2022.11.25
* [ ] v2022.10.26
* [ ] v2022.10.18
* [ ] v2022.10.04
* [ ] v2022.09.27
* [ ] v2022.09.19
* [ ] v2022.09.09
* [ ] v2022.08.07
* [ ] v2022.07.27
* [ ] v2022.06.25

Table of Contents
=======================

* [What is openpilot?](#what-is-openpilot)
* [Running in a car](#running-on-a-dedicated-device-in-a-car)
* [Running on PC](#running-on-pc)
* [Community and Contributing](#community-and-contributing)
* [User Data and comma Account](#user-data-and-comma-account)
* [Safety and Testing](#safety-and-testing)
* [Directory Structure](#directory-structure)
* [Licensing](#licensing)

---

What is openpilot?
------

[openpilot](http://github.com/commaai/openpilot) is an open source driver assistance system. Currently, openpilot performs the functions of Adaptive Cruise Control (ACC), Automated Lane Centering (ALC), Forward Collision Warning (FCW), and Lane Departure Warning (LDW) for a growing variety of [supported car makes, models, and model years](docs/CARS.md). In addition, while openpilot is engaged, a camera-based Driver Monitoring (DM) feature alerts distracted and asleep drivers. See more about [the vehicle integration](docs/INTEGRATION.md) and [limitations](docs/LIMITATIONS.md).

<table>
  <tr>
    <td><a href="https://youtu.be/NmBfgOanCyk" title="Video By Greer Viau"><img src="https://i.imgur.com/1w8c6d2.jpg"></a></td>
    <td><a href="https://youtu.be/VHKyqZ7t8Gw" title="Video By Logan LeGrand"><img src="https://i.imgur.com/LnBucik.jpg"></a></td>
    <td><a href="https://youtu.be/VxiR4iyBruo" title="Video By Charlie Kim"><img src="https://i.imgur.com/4Qoy48c.jpg"></a></td>
    <td><a href="https://youtu.be/-IkImTe1NYE" title="Video By Aragon"><img src="https://i.imgur.com/04VNzPf.jpg"></a></td>
  </tr>
  <tr>
    <td><a href="https://youtu.be/iIUICQkdwFQ" title="Video By Logan LeGrand"><img src="https://i.imgur.com/b1LHQTy.jpg"></a></td>
    <td><a href="https://youtu.be/XOsa0FsVIsg" title="Video By PinoyDrives"><img src="https://i.imgur.com/6FG0Bd8.jpg"></a></td>
    <td><a href="https://youtu.be/bCwcJ98R_Xw" title="Video By JS"><img src="https://i.imgur.com/zO18CbW.jpg"></a></td>
    <td><a href="https://youtu.be/BQ0tF3MTyyc" title="Video By Tsai-Fi"><img src="https://i.imgur.com/eZzelq3.jpg"></a></td>
  </tr>
</table>


Running on a dedicated device in a car
------

To use openpilot in a car, you need four things
* A supported device to run this software: a [comma three](https://comma.ai/shop/products/three).
* This software. The setup procedure of the comma three allows the user to enter a URL for custom software.
The URL, openpilot.comma.ai will install the release version of openpilot. To install openpilot master, you can use installer.comma.ai/commaai/master, and replacing commaai with another GitHub username can install a fork.
* One of [the 250+ supported cars](docs/CARS.md). We support Honda, Toyota, Hyundai, Nissan, Kia, Chrysler, Lexus, Acura, Audi, VW, Ford and more. If your car is not supported but has adaptive cruise control and lane-keeping assist, it's likely able to run openpilot.
* A [car harness](https://comma.ai/shop/products/car-harness) to connect to your car.

We have detailed instructions for [how to mount the device in a car](https://comma.ai/setup).

Running on PC
------

All openpilot services can run as usual on a PC without requiring special hardware or a car. You can also run openpilot on recorded or simulated data to develop or experiment with openpilot.

With openpilot's tools, you can plot logs, replay drives, and watch the full-res camera streams. See [the tools README](tools/README.md) for more information.

You can also run openpilot in simulation [with the CARLA simulator](tools/sim/README.md). This allows openpilot to drive around a virtual car on your Ubuntu machine. The whole setup should only take a few minutes but does require a decent GPU.

A PC running openpilot can also control your vehicle if it is connected to a [webcam](https://github.com/commaai/openpilot/tree/master/tools/webcam), a [black panda](https://comma.ai/shop/products/panda), and a [harness](https://comma.ai/shop/products/car-harness).

Community and Contributing
------

openpilot is developed by [comma](https://comma.ai/) and by users like you. We welcome both pull requests and issues on [GitHub](http://github.com/commaai/openpilot). Bug fixes and new car ports are encouraged. Check out [the contributing docs](docs/CONTRIBUTING.md).

Documentation related to openpilot development can be found on [docs.comma.ai](https://docs.comma.ai). Information about running openpilot (e.g. FAQ, fingerprinting, troubleshooting, custom forks, community hardware) should go on the [wiki](https://github.com/commaai/openpilot/wiki).

You can add support for your car by following guides we have written for [Brand](https://blog.comma.ai/how-to-write-a-car-port-for-openpilot/) and [Model](https://blog.comma.ai/openpilot-port-guide-for-toyota-models/) ports. Generally, a car with adaptive cruise control and lane keep assist is a good candidate. [Join our Discord](https://discord.comma.ai) to discuss car ports: most car makes have a dedicated channel.

Want to get paid to work on openpilot? [comma is hiring](https://comma.ai/jobs#open-positions).

And [follow us on Twitter](https://twitter.com/comma_ai).

User Data and comma Account
------

By default, openpilot uploads the driving data to our servers. You can also access your data through [comma connect](https://connect.comma.ai/). We use your data to train better models and improve openpilot for everyone.

openpilot is open source software: the user is free to disable data collection if they wish to do so.

openpilot logs the road-facing cameras, CAN, GPS, IMU, magnetometer, thermal sensors, crashes, and operating system logs.
The driver-facing camera is only logged if you explicitly opt-in in settings. The microphone is not recorded.

By using openpilot, you agree to [our Privacy Policy](https://comma.ai/privacy). You understand that use of this software or its related services will generate certain types of user data, which may be logged and stored at the sole discretion of comma. By accepting this agreement, you grant an irrevocable, perpetual, worldwide right to comma for the use of this data.

Safety and Testing
----

* openpilot observes ISO26262 guidelines, see [SAFETY.md](docs/SAFETY.md) for more details.
* openpilot has software-in-the-loop [tests](.github/workflows/selfdrive_tests.yaml) that run on every commit.
* The code enforcing the safety model lives in panda and is written in C, see [code rigor](https://github.com/commaai/panda#code-rigor) for more details.
* panda has software-in-the-loop [safety tests](https://github.com/commaai/panda/tree/master/tests/safety).
* Internally, we have a hardware-in-the-loop Jenkins test suite that builds and unit tests the various processes.
* panda has additional hardware-in-the-loop [tests](https://github.com/commaai/panda/blob/master/Jenkinsfile).
* We run the latest openpilot in a testing closet containing 10 comma devices continuously replaying routes.

Directory Structure
------
    .
    ├── cereal              # The messaging spec and libs used for all logs
    ├── common              # Library like functionality we've developed here
    ├── docs                # Documentation
    ├── opendbc             # Files showing how to interpret data from cars
    ├── panda               # Code used to communicate on CAN
    ├── third_party         # External libraries
    ├── pyextra             # Extra python packages
    └── system              # Generic services
        ├── camerad         # Driver to capture images from the camera sensors
        ├── clocksd         # Broadcasts current time
        ├── hardware        # Hardware abstraction classes
        ├── logcatd         # systemd journal as a service
        ├── loggerd         # Logger and uploader of car data
        ├── proclogd        # Logs information from /proc
        ├── sensord         # IMU interface code
        └── ubloxd          # u-blox GNSS module interface code
    └── selfdrive           # Code needed to drive the car
        ├── assets          # Fonts, images, and sounds for UI
        ├── athena          # Allows communication with the app
        ├── boardd          # Daemon to talk to the board
        ├── car             # Car specific code to read states and control actuators
        ├── controls        # Planning and controls
        ├── debug           # Tools to help you debug and do car ports
        ├── locationd       # Precise localization and vehicle parameter estimation
        ├── manager         # Daemon that starts/stops all other daemons as needed
        ├── modeld          # Driving and monitoring model runners
        ├── monitoring      # Daemon to determine driver attention
        ├── navd            # Turn-by-turn navigation
        ├── test            # Unit tests, system tests, and a car simulator
        └── ui              # The UI

Licensing
------

openpilot is released under the MIT license. Some parts of the software are released under other licenses as specified.

Any user of this software shall indemnify and hold harmless Comma.ai, Inc. and its directors, officers, employees, agents, stockholders, affiliates, subcontractors and customers from and against all allegations, claims, actions, suits, demands, damages, liabilities, obligations, losses, settlements, judgments, costs and expenses (including without limitation attorneys’ fees and costs) which arise out of, relate to or result from any use of this software by user.

**THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.
YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.
NO WARRANTY EXPRESSED OR IMPLIED.**

---

<img src="https://d1qb2nb5cznatu.cloudfront.net/startups/i/1061157-bc7e9bf3b246ece7322e6ffe653f6af8-medium_jpg.jpg?buster=1458363130" width="75"></img> <img src="https://cdn-images-1.medium.com/max/1600/1*C87EjxGeMPrkTuVRVWVg4w.png" width="225"></img>

[![openpilot tests](https://github.com/commaai/openpilot/workflows/openpilot%20tests/badge.svg?event=push)](https://github.com/commaai/openpilot/actions)
[![codecov](https://codecov.io/gh/commaai/openpilot/branch/master/graph/badge.svg)](https://codecov.io/gh/commaai/openpilot)
