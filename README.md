# VPS-Service-Manager

|Part|Language|
|:---|:-------|
|**Web Interface**|HTML/CSS/JS(NGINX)|
|**REST API**|TypeScript(Express)|
|**Service Manager**|Python|
|**Service Start Scripts**|Bash|

## (Work-In-Progress) graph of how it kinda works
```mermaid
graph TB;
    WI[Web Interface -client-]
    API[REST API]
    SM[Service Manager]
    SS[Service Start Scripts]
    DB{SQLite DB}

    subgraph Public
    WI-->|Internet|API
    end

    subgraph Local
    API-->|Config.json|SM
    SM-->SS
    end
```
