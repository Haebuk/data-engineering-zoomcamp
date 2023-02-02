from prefect.infrastructure.docker import DockerContainer

# alternative to creating docker container block in the UI
docker_container_block = DockerContainer(
    image="cwryu6252/prefect:zoom",
    image_pull_policy="ALWAYS",
    auto_remove=True,
)

docker_container_block.save("zoom", overwrite=True)