# Supervisor Watcher

[![Build Status](https://travis-ci.org/dskoda1/supervisor-watcher.svg?branch=master)](https://travis-ci.org/dskoda1/supervisor-watcher)

## About

Love using [Supervisor](https://github.com/Supervisor/supervisor) to watch your
python processes?

Hate that you can't view the status of each one without going to a different
webpage?

Well finally the solution is here! Just spin this little flask service up, add
your supervisor hosts, and view them all in once concise format!


## Quick Start

1. Run the development server (this creates a virualenv if non existent):

  ```
  $ make server
  ```

  Navigate to [http://localhost:5000](http://localhost:5000)

2. Test:

  ```
  $ make test
  ```


Thanks [Flask Boilerplate](https://github.com/mjhea0/flask-boilerplate/tree/updated) for helping!
