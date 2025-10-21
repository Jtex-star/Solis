from pydantic import BaseSettings, Field, constr, conint
from typing import List

class APISettings(BaseSettings):
    api_key: constr(min_length=1) = Field(..., env='API_KEY')
    api_secret: constr(min_length=1) = Field(..., env='API_SECRET')

class AWSSettings(BaseSettings):
    access_key: constr(min_length=1) = Field(..., env='AWS_ACCESS_KEY')
    secret_key: constr(min_length=1) = Field(..., env='AWS_SECRET_KEY')
    region: constr(min_length=1) = Field(..., env='AWS_REGION')

class KafkaSettings(BaseSettings):
    bootstrap_servers: List[str] = Field(..., env='KAFKA_BOOTSTRAP_SERVERS')
    topic: constr(min_length=1) = Field(..., env='KAFKA_TOPIC')
    group_id: constr(min_length=1) = Field(..., env='KAFKA_GROUP_ID')

class RateLimitSettings(BaseSettings):
    requests_per_minute: conint(ge=1) = Field(..., env='RATE_LIMIT_REQUESTS_PER_MINUTE')

class CircuitBreakerSettings(BaseSettings):
    failure_threshold: conint(ge=0) = Field(..., env='CIRCUIT_BREAKER_FAILURE_THRESHOLD')
    recovery_timeout: conint(gt=0) = Field(..., env='CIRCUIT_BREAKER_RECOVERY_TIMEOUT')

class PerformanceTuningSettings(BaseSettings):
    max_connections: conint(gt=0) = Field(..., env='MAX_CONNECTIONS')
    timeout: conint(gt=0) = Field(..., env='TIMEOUT')

class DataQualitySettings(BaseSettings):
    min_quality_score: conint(ge=0, le=100) = Field(..., env='MIN_QUALITY_SCORE')

class StorageOptions(BaseSettings):
    database_url: constr(min_length=1) = Field(..., env='DATABASE_URL')
    backup_location: constr(min_length=1) = Field(..., env='BACKUP_LOCATION')

class Settings(BaseSettings):
    api: APISettings
    aws: AWSSettings
    kafka: KafkaSettings
    rate_limit: RateLimitSettings
    circuit_breaker: CircuitBreakerSettings
    performance_tuning: PerformanceTuningSettings
    data_quality: DataQualitySettings
    storage: StorageOptions

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()