create table document
(
    document_id varchar(64)                           not null
        primary key,
    uuid        varchar(64)                           not null,
    name        varchar(255)                          null,
    status      varchar(64) default 'uncompleted'     null,
    create_time timestamp   default CURRENT_TIMESTAMP null,
    constraint document_document_id_uindex
        unique (document_id),
    constraint document_uuid_uindex
        unique (uuid)
);

