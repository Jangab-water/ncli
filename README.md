# NCLI

## 목적

Cloud Function에서 구동 가능한 경량 모니터링 소프트웨어 제작. 지속적인 훅을 날리는게 아닌, 매일의 결과를 정리해 리포팅하는 정도면 충분함.

## 기능상세

1. Ncloud API

- [인증 헤더 생성](https://api.ncloud-docs.com/docs/common-ncpapi)

2. Object Storage

- [미완료 MultiPartUpload 조회](https://api.ncloud-docs.com/docs/storage-objectstorage-listmultipartuploads)

3. CertificateManager

- [만료 예정 SSL 인증서 조회](https://api.ncloud-docs.com/docs/security-certificatemanager-getcertificatelist)

4. SecurityMonitoring

- [백신 이벤트 조회](https://api.ncloud-docs.com/docs/security-securitymonitoring-getavlist)

- [DDoS 이벤트 조회](https://api.ncloud-docs.com/docs/security-securitymonitoring-getddoslist)

- [IDS 이벤트 조회](https://api.ncloud-docs.com/docs/security-securitymonitoring-getidslist)

- [IPS 이벤트 조회](https://api.ncloud-docs.com/docs/security-securitymonitoring-getipslist)

- [WAF 이벤트 조회](https://api.ncloud-docs.com/docs/security-securitymonitoring-getwaflist)

5. Monitoring

- [통계 정보 조회](https://api.ncloud-docs.com/docs/management-monitoring-getmetricstatisticlist)

- [통계 수집 대상 조회](https://api.ncloud-docs.com/docs/management-monitoring-getlistmetrics)

6. Cloud Activity Tracer

- [클라우드 인프라 변경사항 조회](https://api.ncloud-docs.com/docs/management-cloudactivitytracer-getactivitylist)

7. Cloud Acvisor

- [클라우드 설정 권장사항 조회](https://api.ncloud-docs.com/docs/management-cloud-advisor-refresh) - 추가 확인 필요

