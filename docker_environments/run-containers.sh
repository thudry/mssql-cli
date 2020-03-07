# Runs docker containers for each supported Linux distribution
# Enables easier interactive mode testing

if [ -z "$1" ]
  then
    echo "Argument should be path to local repo."
    exit 1
fi

local_repo=$1
docker_dir='linux-direct-stable'

for dir in $local_repo/$docker_dir/*; do
    dist_name=${dir##*/}
    tag_name=mssqlcli:$dist_name

    echo "RUNNING CONTAINER FOR: $dist_name\n"

    # run container
    docker run -it $tag_name bash
    
    echo "\n\n"
done
