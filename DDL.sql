CREATE DATABASE proyecto_python_flask
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Venezuela.1252'
    LC_CTYPE = 'Spanish_Venezuela.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
CREATE TABLE IF NOT EXISTS public.clientes
(
    cedula integer NOT NULL,
    nombre character varying(50) COLLATE pg_catalog."default" NOT NULL,
    whatsapp character varying(20) COLLATE pg_catalog."default",
    email character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT clientes_pkey PRIMARY KEY (cedula)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clientes
    OWNER to postgres;
	
CREATE TABLE IF NOT EXISTS public.pedidos
(
    order_number integer NOT NULL DEFAULT nextval('pedidos_order_number_seq'::regclass),
    payment_method character varying(50) COLLATE pg_catalog."default",
    quantity integer,
    remarks text COLLATE pg_catalog."default",
    city character varying(30) COLLATE pg_catalog."default",
    municipality character varying(35) COLLATE pg_catalog."default",
    cedula integer,
    payments_screenshot bytea,
    status character varying(20) COLLATE pg_catalog."default",
    delivery_amount character varying(10) COLLATE pg_catalog."default" NOT NULL,
    datatime timestamp without time zone,
    total character varying(15) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT pedidos_pkey PRIMARY KEY (order_number),
    CONSTRAINT pedidos_cedula_fkey FOREIGN KEY (cedula)
        REFERENCES public.clientes (cedula) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.pedidos
    OWNER to postgres;