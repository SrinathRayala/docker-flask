import docker
#client = docker.from_env(environment={'DOCKER_HOST':'tcp://3.135.218.148:2375'})
client = docker.from_env(environment={'DOCKER_HOST':'tcp://34.66.188.118:2375'})

def list_containers() :
    containers_list = client.containers.list(all=True)
    containers = map(lambda container:
                   {
                       'container_id': container.short_id,
                       'container_name': container.name,
                       'container_status': container.status
                   }, containers_list)
    return list(containers)
def list_images():
    images_list = client.images.list(all=True)
    images = map(lambda image:
                     {
                         'container_id': image.short_id,
                         'container_name': 'No Tag' if len(image.tags) == 0 else image.tags[0],
                     }, images_list)
    return list(images)
def manage_container(containder_id,action):
    container =client.containers.get(containder_id)
    if action == 'stop':
        container.stop()
    elif action == 'start':
        container.start()
    else:
        container.remove()
