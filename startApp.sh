#!/bin/bash
BLUE='\033[1;34m'
NC='\033[0m' # No Color

printf "${BLUE}=== Starting the app setup ===${NC}\n"

# Create network if not exists
printf "${BLUE}Checking Docker network 'tsds-network'...${NC}\n"
if docker network ls | grep -q tsds-network; then
    printf "${BLUE}Network 'tsds-network' already exists${NC}\n"
else
    printf "${BLUE}Creating network 'tsds-network'...${NC}\n"
    docker network create tsds-network
    printf "${BLUE}Network created${NC}\n"
fi

# Pull latest images from Docker Hub
printf "${BLUE}Pulling backend image from Docker Hub...${NC}\n"
docker pull sharadaraghunatha/tsdsbackend:latest
printf "${BLUE}Backend image pulled${NC}\n"

printf "${BLUE}Pulling frontend image from Docker Hub...${NC}\n"
docker pull sharadaraghunatha/tsdsfrontend:latest
printf "${BLUE}Frontend image pulled${NC}\n"


# Remove old containers if they exist
printf "${BLUE}Removing old containers if they exist...${NC}\n"
docker rm -f tsdsbackend tsdsfrontend 2>/dev/null
printf "${BLUE}Old containers removed (if any)${NC}\n"

# Run backend container
printf "${BLUE}Starting backend container...${NC}\n"
docker run -d \
  --name tsdsbackend \
  --network tsds-network \
  sharadaraghunatha/tsdsbackend:latest
printf "${BLUE}Backend container started${NC}\n"

# Run frontend container
printf "${BLUE}Starting frontend container...${NC}\n"
docker run -d --name tsdsfrontend --network tsds-network -p 8080:80 
docker run -d \
  --name tsdsfrontend \
  --network tsds-network \
  -p 8080:80 \
  sharadaraghunatha/tsdsfrontend:latest
printf "${BLUE}Frontend container started${NC}\n"

printf "${BLUE}=== App setup complete! You can access the frontend at http://localhost:8080 ===${NC}\n"
