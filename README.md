# Identify Features that Drive Retention

A Python script that analyzes user engagement data for a mobile app to identify
features that drive user retention. Using a cohort analysis, it finds that users
who engaged with a specific feature within their first week were more likely to
remain active after 3 months.

## Installation

You must have git and Python installed.

Clone this repository.

```sh
git clone https://github.com/travishorn/identify_retention
```

Change into the directory.

```sh
cd identify_retention
```

Install the dependencies.

```sh
pip install -r requirements.txt
```

## Usage

Look at `dataset.csv` to get an idea of what the data looks like

Run the script.

```sh
python main.py
```

Output is printed to the terminal.

## Interpreting Results

```
Retention rates for users engaging with features in the first week:
feature_a_used: 83.56%
feature_b_used: 64.37%
feature_c_used: 66.39%
```

Users who engage with Feature A in their first week have an 84% retention rate
after 3 months, significantly higher than those engaging with Feature B (64%) or
Feature C (66%). This suggests Feature A is particularly effective at retaining
engagement.

Feature B and C also contribute, but not as strongly as Feature A.

### Suggestions

- Encourage new users to interact with Feature A during their first week.
- Highlight Feature A in the UI.
- Create tutorials or incentives to showcase Feature A's value.
- Investigate why Feature A is effective and replicate it for other features.
- What pain points does it address?
- Does it provide immediate or long-term benefit?
- Is it easy to use?
- Experiment with feature pairing and synergy between Feature A and other
  features.

## License

The MIT License

Copyright 2024 Travis Horn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
