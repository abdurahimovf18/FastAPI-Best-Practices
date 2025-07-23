set -e

REPLICA_COUNT=${REPLICA_COUNT:-1}
CPU_COUNT=$(nproc)

if [ "$REPLICA_COUNT" -lt 1 ]; then
  echo "Invalid REPLICA_COUNT: $REPLICA_COUNT"
  exit 1
fi

CPU_PER_REPLICA=$(( CPU_COUNT / REPLICA_COUNT ))

WORKER_COUNT=$(( CPU_PER_REPLICA * 2 + 1 ))

echo "CPU_COUNT=$CPU_COUNT"
echo "REPLICA_COUNT=$REPLICA_COUNT"
echo "Starting with $WORKER_COUNT workers..."

exec uv run gunicorn src.service.api.main:app \
  --workers "$WORKER_COUNT" \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
