create table sentence
(
    sentence_id        varchar(64) not null
        primary key,
    belong_document_id varchar(64) not null,
    sequence           int         not null,
    context            json        null,
    constraint sentence_id_uindex
        unique (sentence_id)
);

