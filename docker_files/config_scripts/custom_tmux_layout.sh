 #!/bin/bash

  # Start a new tmux session detached
  tmux new-session -d -s mySession

  # Split the window into two horizontal panes, with the right pane being 50% of the screen width
  tmux split-window -h -p 50

  tmux split-window -v -p 30

  # Attach to the session
  tmux attach-session -t mySession