NetClock Server
===============

This module contains the server program for the ECE 4564 NetClock project.

The server program is designed to run as a Python runnable module. As
such, this directory contains an empty `__init__.py` and a `__main__.py`.
In `__main__.py`, you'll find that an argument parser has been created
and configured with the options that you're likely to want/need when
implementing the server. The main entry point parses the command line,
and configures the logging framework first. It then creates the
SubscriberRepository and ClockServer objects and invokes the server's
`run` method.

In `server.py`, you'll find a stub for the ClockServer implementation.
The ClockServer is responsible for listening for client subscription
messages, periodically broadcasting date and time updates to all 
subscribers, and aging the collection of subscribers to detect and
remove subscriptions for clients that have not renewed their subscriptions.

The ClockServer object uses with the SubscriberRepository object
to keep a persistent record of all subscribers. In `repository.py` you'll
find a stub for your SubscriberRepository implementation. The repository
will use a Queue to accept requests to add and remove subscribers (from
the ClockServer). It will use a dedicated thread to service the queue, so
that the server is never delayed by the I/O needed to save the current
set of subscribers after each add or remove.

See the comments in the `server.py` and `repository.py` for the methods 
your team must implement. Review the project design blueprint for additional 
guidance on how to implement your server program.


Running the Server: Mac OS X
----------------------------

Open a terminal and set the shell's current directory to the base directory of
the project (the one containing `requirements.txt` and the `src` directory).

Run the following commands.
```
export PYTHONPATH=src
python3 -m clock_server subscribers.json
```

There are lots of other command line options that can be specified; run the
same Python command with the `-h` (`--help`) option for details.

Running the Server: Windows
---------------------------

Open a command prompt and set the current directory to the base directory of
the project (the one containing `requirements.txt` and the `src` directory).

Run the following commands.
```
set PYTHONPATH=src
py -m clock_server subscribers.json
```

There are lots of other command line options that can be specified; run the
same Python command with the `-h` (`--help`) option for details.

### Windows Notes
* The server process doesn't always seem to respond to Ctrl-C on Windows. If
  necessary, use Task Manager to kill the server process.
* Windows seems to sporadically report "[WinError 10054] An existing connection 
  was forcibly by the remote host" on UDP sockets.

==============================================================================================================================================================================================


NetClock Client
===============

This module contains the client program for the ECE 4564 NetClock project.

To the Project Team:
--------------------

Another development team has created a cross-platform UI that simulates 
the clock display that will be used in the product, as well as a simple 
chronometer that keeps time based on an interval timer and a tick
counter. The chronometer is reasonably accurate over relatively short
time periods, but must be occasionally updated from a network date
and time source in order to remain accurate over longer periods of time.

In addition to the UI and chronometer, a `__main__.py` entry point has been
provided that includes an argument parser, logging configuration, and the 
setup for the main program.

Your team will need to implement the ClockClient class using the stub
provided in `client.py`. The client ClockClient class is responsible for
registering with the server as a subscriber, periodically renewing the
subscription, and processing the periodic date/time broadcasts from the
server to update the chronometer. 

See the comments in the file for the methods your client must implement 
in order to interface with the main program. Review the project design 
blueprint for additional guidance on how to implement your client 
communication module for the clock.

While your team doesn't need a detailed understanding of all the 
components of the client program, you should familiarize yourselves with
the location and basic purpose of each of the components provided to you.

* `__main__.py` is the main entry point, which creates the component objects
  of the client program, starts the client communication module (which runs
  on a separate thread), and the calls the clock UI's `run` method to keep
  the simulated clock UI fresh.
* `chronometer.py` contains the Chronometer class which implements the
  timekeeping functions for the clock. The passage of time is measured using
  a thread to periodically sample a high resolution tick counter.
* `instant.py` is an object that represents an instant in time as a 
  set of related attributes (year, month, day, hour, minute, etc). An 
  Instant object has an `incr` method that can be used to produce a new 
  Instant by adding a number of microseconds to itself.
* `ui/` is the package that contains code for the client's clock user 
  interface. The clock display uses simulated common LED display units 
  consisting of 7 or 14 LED segments. The code in this module uses
  [pygame](https://pygame.org) to create a drawing surface on which it draws
  and fills polygons representing each LED segment of each display unit. The 
  main UI class is the ClockUI class found in `clock.py`. It sets up the clock
  display and runs the main loop that updates the clock. It gets a reference
  to the Chronometer's `read` method which it uses to poll the current date
  and time as it updates the display.


Running the Client Program
--------------------------

The client program is designed to be run as a Python runnable module.

Because the client program uses the [pygame](https://pygame.org) library
you'll need to install this library in order to run the client. 

The easiest approach is simply to install the pygame library directly into your Python enviroment. Another approach is to use a [Python Virtual Environment](https://docs.python.org/3/tutorial/venv.html). The instructions below take
the easier approach, but feel free to use a virtual environment if you prefer.

The instructions vary by plaform.

### Mac OS X

#### Install the required library

Open a terminal and set the shell's current directory to the base directory of
the project (the one containing `requirements.txt` and the `src` directory).

Run the following command to install the required library.
```
python3 -m pip install -r requirements.txt
```

When the command above has completed successfully, the library is installed and
you needn't perform this step again.

#### Run the client

Open a terminal and set the shell's current directory to the base directory of
the project (the one containing `requirements.txt` and the `src` directory).

Run the client using the following commands.
```
export PYTHONPATH=src
python3 -m clock_client 127.0.0.1
```

The client supports several different colors and sizes for the UI. To learn 
about all the options, run the same Python command with the `-h` (`--help`) 
option.

### Windows

#### Install the required library

Open a command prompt and set the current directory to the base directory of
the project (the one containing `requirements.txt` and the `src` directory).

Run the following command to install the required library.
```
py -m pip install -r requirements.txt
```

When the command above has completed successfully, the library is installed and
you needn't perform this step again.

#### Run the client

Open a command prompt and set the current directory to the base directory of
the project (the one containing `requirements.txt` and the `src` directory).

Run the client using the following commands.
```
set PYTHONPATH=src
py -m clock_client 127.0.0.1
```

The client supports several different colors and sizes for the UI. To learn 
about all the options, run the same Python command with the `-h` (`--help`) 
option.

