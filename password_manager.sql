PGDMP         :                 y            password_manager    13.1    13.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16394    password_manager    DATABASE     t   CREATE DATABASE password_manager WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
     DROP DATABASE password_manager;
                postgres    false            �            1259    16395    accounts    TABLE     �   CREATE TABLE public.accounts (
    password character varying,
    user_email character varying,
    username character varying,
    url character varying,
    app_name character varying
);
    DROP TABLE public.accounts;
       public         heap    postgres    false            �          0    16395    accounts 
   TABLE DATA           Q   COPY public.accounts (password, user_email, username, url, app_name) FROM stdin;
    public          postgres    false    200   �       �     x�]�[k�@��wE������Ѐ�IJ�$�J_F�����1����tU��0��ff-�����F���O����ρfJ�r4Ba�ëﳙ��?.�jY]���H�^��V�.�Ï���_5)c�9%�i!f�m�F� $c� ��w����=ӽ%ʡ���frȡ��f��V��ɶ�g�������%]�X�"��^�����R�?ߥ-*XA���5�⭠G�KZ�ʒ��p)���xI�L5w�S��<�C����z��AM)�T0ƿ�Q�     