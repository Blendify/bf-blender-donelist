Command to get an git-log with rst-roles pre-defined.

.. code-block:: sh

   html_term -o gitlog.html -c 'git log \
         --stat \
         --decorate \
         --format="%C(yellow):commit:\`B%H\` ~ %cd%n %C(green) %B%Creset" \
         --author="Aaron Carlisle" \
         61c66a996ca5e590097e8864df027602493f58f4..HEAD | \
         perl -e "s/\bT(\d+)\b/:task:\`\$1\`/" -pi | \
         perl -e "s/\bD(\d+)\b/:diff:\`\$1\`/" -pi'

