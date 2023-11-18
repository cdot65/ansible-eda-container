"""Tasks to execute with Invoke."""

# ---------------------------------------------------------------------------
# Python3.11 hack for invoke
# ---------------------------------------------------------------------------
import inspect

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

import os
from invoke import task

# ---------------------------------------------------------------------------
# CONTAINER PARAMETERS
# ---------------------------------------------------------------------------
CONTAINER_IMG = "ghcr.io/cdot65/ansible-eda"
CONTAINER_TAG = "0.0.1"


# ---------------------------------------------------------------------------
# SYSTEM PARAMETERS
# ---------------------------------------------------------------------------
PWD = os.getcwd()


# ---------------------------------------------------------------------------
# CONTAINER BUILDS
# ---------------------------------------------------------------------------
@task()
def build(context):
    """Build our Container image."""
    build_cmd = f"podman build -t {CONTAINER_IMG}:{CONTAINER_TAG} ./container"
    context.run(
        f"{build_cmd}",
    )


# ---------------------------------------------------------------------------
# CONTAINER IMAGE PUBLISH (are you sure? this is a huge image right now >2GB)
# ---------------------------------------------------------------------------
@task()
def publish(context):
    """Publish our container image."""
    publish_cmd = f"podman push {CONTAINER_IMG}:{CONTAINER_TAG}"
    context.run(
        f"{publish_cmd}",
    )


# ---------------------------------------------------------------------------
# CONTAINER LIFE CYCLE
# ---------------------------------------------------------------------------
@task()
def up(context):
    """Spin up the container."""
    run_cmd = f"""
        podman run -d -p 5000:5000 --name eda {CONTAINER_IMG}:{CONTAINER_TAG} \
            ansible-rulebook --rulebook=eda/rulebooks/example.yaml \
            -i eda/inventory/inventory.yaml --verbose
        """
    context.run(
        f"{run_cmd}",
    )


@task()
def down(context):
    """Spin down the container."""
    stop_cmd = "podman stop eda"
    remove_cmd = "podman rm eda"
    context.run(
        f"{stop_cmd} && {remove_cmd}",
    )


@task()
def logs(context):
    """tail -f the container logs."""
    logs_cmd = "podman logs -f eda"
    context.run(
        f"{logs_cmd}",
    )
