# How To Make a New Tanulib App 

## Step1. Create a new repo in Github

Go to github and create a new repo.

## Step2. Clone the repo at local machine

```bash
git clone -b <working branch name> git@github.com:<account name>/<repo name>.git
```

## Step3. Create virtual env

Run the below

```bash
python3 -m venv [virtual env name]
# e.g. python3 -m venv .venv
```

If you are using VSC, after restarting VSC, VSC shows a prompt to source the venv's activate.

## Step4A. Install Tanukilib from local

```bash
pip3 install -e <local tanukilib project's homedir>/tanukilib
```

## Step5. Verify

Make sure your app with tanukilib works

```python3
from tlib.datautil import round_to_nearest_half_down

def main():
    print("hello tlib app")
    f = 31.2345
    print(round_to_nearest_half_down(f, 3))
    

if __name__ == "__main__":
    main()
```
