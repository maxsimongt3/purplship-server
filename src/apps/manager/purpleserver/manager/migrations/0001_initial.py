# Generated by Django 3.1.2 on 2020-10-21 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import functools
import jsonfield.fields
import purpleserver.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('providers', '0002_carrier_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'adr_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('federal_tax_id', models.CharField(blank=True, max_length=50, null=True)),
                ('state_tax_id', models.CharField(blank=True, max_length=50, null=True)),
                ('person_name', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country_code', models.CharField(choices=[('AD', 'AD'), ('AE', 'AE'), ('AF', 'AF'), ('AG', 'AG'), ('AI', 'AI'), ('AL', 'AL'), ('AM', 'AM'), ('AN', 'AN'), ('AO', 'AO'), ('AR', 'AR'), ('AS', 'AS'), ('AT', 'AT'), ('AU', 'AU'), ('AW', 'AW'), ('AZ', 'AZ'), ('BA', 'BA'), ('BB', 'BB'), ('BD', 'BD'), ('BE', 'BE'), ('BF', 'BF'), ('BG', 'BG'), ('BH', 'BH'), ('BI', 'BI'), ('BJ', 'BJ'), ('BM', 'BM'), ('BN', 'BN'), ('BO', 'BO'), ('BR', 'BR'), ('BS', 'BS'), ('BT', 'BT'), ('BW', 'BW'), ('BY', 'BY'), ('BZ', 'BZ'), ('CA', 'CA'), ('CD', 'CD'), ('CF', 'CF'), ('CG', 'CG'), ('CH', 'CH'), ('CI', 'CI'), ('CK', 'CK'), ('CL', 'CL'), ('CM', 'CM'), ('CN', 'CN'), ('CO', 'CO'), ('CR', 'CR'), ('CU', 'CU'), ('CV', 'CV'), ('CY', 'CY'), ('CZ', 'CZ'), ('DE', 'DE'), ('DJ', 'DJ'), ('DK', 'DK'), ('DM', 'DM'), ('DO', 'DO'), ('DZ', 'DZ'), ('EC', 'EC'), ('EE', 'EE'), ('EG', 'EG'), ('ER', 'ER'), ('ES', 'ES'), ('ET', 'ET'), ('FI', 'FI'), ('FJ', 'FJ'), ('FK', 'FK'), ('FM', 'FM'), ('FO', 'FO'), ('FR', 'FR'), ('GA', 'GA'), ('GB', 'GB'), ('GD', 'GD'), ('GE', 'GE'), ('GF', 'GF'), ('GG', 'GG'), ('GH', 'GH'), ('GI', 'GI'), ('GL', 'GL'), ('GM', 'GM'), ('GN', 'GN'), ('GP', 'GP'), ('GQ', 'GQ'), ('GR', 'GR'), ('GT', 'GT'), ('GU', 'GU'), ('GW', 'GW'), ('GY', 'GY'), ('HK', 'HK'), ('HN', 'HN'), ('HR', 'HR'), ('HT', 'HT'), ('HU', 'HU'), ('IC', 'IC'), ('ID', 'ID'), ('IE', 'IE'), ('IL', 'IL'), ('IN', 'IN'), ('IQ', 'IQ'), ('IR', 'IR'), ('IS', 'IS'), ('IT', 'IT'), ('JE', 'JE'), ('JM', 'JM'), ('JO', 'JO'), ('JP', 'JP'), ('KE', 'KE'), ('KG', 'KG'), ('KH', 'KH'), ('KI', 'KI'), ('KM', 'KM'), ('KN', 'KN'), ('KP', 'KP'), ('KR', 'KR'), ('KV', 'KV'), ('KW', 'KW'), ('KY', 'KY'), ('KZ', 'KZ'), ('LA', 'LA'), ('LB', 'LB'), ('LC', 'LC'), ('LI', 'LI'), ('LK', 'LK'), ('LR', 'LR'), ('LS', 'LS'), ('LT', 'LT'), ('LU', 'LU'), ('LV', 'LV'), ('LY', 'LY'), ('MA', 'MA'), ('MC', 'MC'), ('MD', 'MD'), ('ME', 'ME'), ('MG', 'MG'), ('MH', 'MH'), ('MK', 'MK'), ('ML', 'ML'), ('MM', 'MM'), ('MN', 'MN'), ('MO', 'MO'), ('MP', 'MP'), ('MQ', 'MQ'), ('MR', 'MR'), ('MS', 'MS'), ('MT', 'MT'), ('MU', 'MU'), ('MV', 'MV'), ('MW', 'MW'), ('MX', 'MX'), ('MY', 'MY'), ('MZ', 'MZ'), ('NA', 'NA'), ('NC', 'NC'), ('NE', 'NE'), ('NG', 'NG'), ('NI', 'NI'), ('NL', 'NL'), ('NO', 'NO'), ('NP', 'NP'), ('NR', 'NR'), ('NU', 'NU'), ('NZ', 'NZ'), ('OM', 'OM'), ('PA', 'PA'), ('PE', 'PE'), ('PF', 'PF'), ('PG', 'PG'), ('PH', 'PH'), ('PK', 'PK'), ('PL', 'PL'), ('PR', 'PR'), ('PT', 'PT'), ('PW', 'PW'), ('PY', 'PY'), ('QA', 'QA'), ('RE', 'RE'), ('RO', 'RO'), ('RS', 'RS'), ('RU', 'RU'), ('RW', 'RW'), ('SA', 'SA'), ('SB', 'SB'), ('SC', 'SC'), ('SD', 'SD'), ('SE', 'SE'), ('SG', 'SG'), ('SH', 'SH'), ('SI', 'SI'), ('SK', 'SK'), ('SL', 'SL'), ('SM', 'SM'), ('SN', 'SN'), ('SO', 'SO'), ('SR', 'SR'), ('SS', 'SS'), ('ST', 'ST'), ('SV', 'SV'), ('SY', 'SY'), ('SZ', 'SZ'), ('TC', 'TC'), ('TD', 'TD'), ('TG', 'TG'), ('TH', 'TH'), ('TJ', 'TJ'), ('TL', 'TL'), ('TN', 'TN'), ('TO', 'TO'), ('TR', 'TR'), ('TT', 'TT'), ('TV', 'TV'), ('TW', 'TW'), ('TZ', 'TZ'), ('UA', 'UA'), ('UG', 'UG'), ('US', 'US'), ('UY', 'UY'), ('UZ', 'UZ'), ('VA', 'VA'), ('VC', 'VC'), ('VE', 'VE'), ('VG', 'VG'), ('VI', 'VI'), ('VN', 'VN'), ('VU', 'VU'), ('WS', 'WS'), ('XB', 'XB'), ('XC', 'XC'), ('XE', 'XE'), ('XM', 'XM'), ('XN', 'XN'), ('XS', 'XS'), ('XY', 'XY'), ('YE', 'YE'), ('YT', 'YT'), ('ZA', 'ZA'), ('ZM', 'ZM'), ('ZW', 'ZW')], max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('state_code', models.CharField(blank=True, max_length=20, null=True)),
                ('suburb', models.CharField(blank=True, max_length=20, null=True)),
                ('residential', models.BooleanField(null=True)),
                ('address_line1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'cdt_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('value_amount', models.FloatField(blank=True, null=True)),
                ('value_currency', models.CharField(blank=True, choices=[('AD', 'AD'), ('AE', 'AE'), ('AF', 'AF'), ('AG', 'AG'), ('AI', 'AI'), ('AL', 'AL'), ('AM', 'AM'), ('AN', 'AN'), ('AO', 'AO'), ('AR', 'AR'), ('AS', 'AS'), ('AT', 'AT'), ('AU', 'AU'), ('AW', 'AW'), ('AZ', 'AZ'), ('BA', 'BA'), ('BB', 'BB'), ('BD', 'BD'), ('BE', 'BE'), ('BF', 'BF'), ('BG', 'BG'), ('BH', 'BH'), ('BI', 'BI'), ('BJ', 'BJ'), ('BM', 'BM'), ('BN', 'BN'), ('BO', 'BO'), ('BR', 'BR'), ('BS', 'BS'), ('BT', 'BT'), ('BW', 'BW'), ('BY', 'BY'), ('BZ', 'BZ'), ('CA', 'CA'), ('CD', 'CD'), ('CF', 'CF'), ('CG', 'CG'), ('CH', 'CH'), ('CI', 'CI'), ('CK', 'CK'), ('CL', 'CL'), ('CM', 'CM'), ('CN', 'CN'), ('CO', 'CO'), ('CR', 'CR'), ('CU', 'CU'), ('CV', 'CV'), ('CY', 'CY'), ('CZ', 'CZ'), ('DE', 'DE'), ('DJ', 'DJ'), ('DK', 'DK'), ('DM', 'DM'), ('DO', 'DO'), ('DZ', 'DZ'), ('EC', 'EC'), ('EE', 'EE'), ('EG', 'EG'), ('ER', 'ER'), ('ES', 'ES'), ('ET', 'ET'), ('FI', 'FI'), ('FJ', 'FJ'), ('FK', 'FK'), ('FM', 'FM'), ('FO', 'FO'), ('FR', 'FR'), ('GA', 'GA'), ('GB', 'GB'), ('GD', 'GD'), ('GE', 'GE'), ('GF', 'GF'), ('GG', 'GG'), ('GH', 'GH'), ('GI', 'GI'), ('GL', 'GL'), ('GM', 'GM'), ('GN', 'GN'), ('GP', 'GP'), ('GQ', 'GQ'), ('GR', 'GR'), ('GT', 'GT'), ('GU', 'GU'), ('GW', 'GW'), ('GY', 'GY'), ('HK', 'HK'), ('HN', 'HN'), ('HR', 'HR'), ('HT', 'HT'), ('HU', 'HU'), ('IC', 'IC'), ('ID', 'ID'), ('IE', 'IE'), ('IL', 'IL'), ('IN', 'IN'), ('IQ', 'IQ'), ('IR', 'IR'), ('IS', 'IS'), ('IT', 'IT'), ('JE', 'JE'), ('JM', 'JM'), ('JO', 'JO'), ('JP', 'JP'), ('KE', 'KE'), ('KG', 'KG'), ('KH', 'KH'), ('KI', 'KI'), ('KM', 'KM'), ('KN', 'KN'), ('KP', 'KP'), ('KR', 'KR'), ('KV', 'KV'), ('KW', 'KW'), ('KY', 'KY'), ('KZ', 'KZ'), ('LA', 'LA'), ('LB', 'LB'), ('LC', 'LC'), ('LI', 'LI'), ('LK', 'LK'), ('LR', 'LR'), ('LS', 'LS'), ('LT', 'LT'), ('LU', 'LU'), ('LV', 'LV'), ('LY', 'LY'), ('MA', 'MA'), ('MC', 'MC'), ('MD', 'MD'), ('ME', 'ME'), ('MG', 'MG'), ('MH', 'MH'), ('MK', 'MK'), ('ML', 'ML'), ('MM', 'MM'), ('MN', 'MN'), ('MO', 'MO'), ('MP', 'MP'), ('MQ', 'MQ'), ('MR', 'MR'), ('MS', 'MS'), ('MT', 'MT'), ('MU', 'MU'), ('MV', 'MV'), ('MW', 'MW'), ('MX', 'MX'), ('MY', 'MY'), ('MZ', 'MZ'), ('NA', 'NA'), ('NC', 'NC'), ('NE', 'NE'), ('NG', 'NG'), ('NI', 'NI'), ('NL', 'NL'), ('NO', 'NO'), ('NP', 'NP'), ('NR', 'NR'), ('NU', 'NU'), ('NZ', 'NZ'), ('OM', 'OM'), ('PA', 'PA'), ('PE', 'PE'), ('PF', 'PF'), ('PG', 'PG'), ('PH', 'PH'), ('PK', 'PK'), ('PL', 'PL'), ('PR', 'PR'), ('PT', 'PT'), ('PW', 'PW'), ('PY', 'PY'), ('QA', 'QA'), ('RE', 'RE'), ('RO', 'RO'), ('RS', 'RS'), ('RU', 'RU'), ('RW', 'RW'), ('SA', 'SA'), ('SB', 'SB'), ('SC', 'SC'), ('SD', 'SD'), ('SE', 'SE'), ('SG', 'SG'), ('SH', 'SH'), ('SI', 'SI'), ('SK', 'SK'), ('SL', 'SL'), ('SM', 'SM'), ('SN', 'SN'), ('SO', 'SO'), ('SR', 'SR'), ('SS', 'SS'), ('ST', 'ST'), ('SV', 'SV'), ('SY', 'SY'), ('SZ', 'SZ'), ('TC', 'TC'), ('TD', 'TD'), ('TG', 'TG'), ('TH', 'TH'), ('TJ', 'TJ'), ('TL', 'TL'), ('TN', 'TN'), ('TO', 'TO'), ('TR', 'TR'), ('TT', 'TT'), ('TV', 'TV'), ('TW', 'TW'), ('TZ', 'TZ'), ('UA', 'UA'), ('UG', 'UG'), ('US', 'US'), ('UY', 'UY'), ('UZ', 'UZ'), ('VA', 'VA'), ('VC', 'VC'), ('VE', 'VE'), ('VG', 'VG'), ('VI', 'VI'), ('VN', 'VN'), ('VU', 'VU'), ('WS', 'WS'), ('XB', 'XB'), ('XC', 'XC'), ('XE', 'XE'), ('XM', 'XM'), ('XN', 'XN'), ('XS', 'XS'), ('XY', 'XY'), ('YE', 'YE'), ('YT', 'YT'), ('ZA', 'ZA'), ('ZM', 'ZM'), ('ZW', 'ZW')], max_length=3, null=True)),
                ('origin_country', models.CharField(blank=True, choices=[('EUR', 'EUR'), ('AED', 'AED'), ('USD', 'USD'), ('XCD', 'XCD'), ('AMD', 'AMD'), ('ANG', 'ANG'), ('AOA', 'AOA'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('AWG', 'AWG'), ('AZN', 'AZN'), ('BAM', 'BAM'), ('BBD', 'BBD'), ('BDT', 'BDT'), ('XOF', 'XOF'), ('BGN', 'BGN'), ('BHD', 'BHD'), ('BIF', 'BIF'), ('BMD', 'BMD'), ('BND', 'BND'), ('BOB', 'BOB'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('BTN', 'BTN'), ('BWP', 'BWP'), ('BYN', 'BYN'), ('BZD', 'BZD'), ('CAD', 'CAD'), ('CDF', 'CDF'), ('XAF', 'XAF'), ('CHF', 'CHF'), ('NZD', 'NZD'), ('CLP', 'CLP'), ('CNY', 'CNY'), ('COP', 'COP'), ('CRC', 'CRC'), ('CUC', 'CUC'), ('CVE', 'CVE'), ('CZK', 'CZK'), ('DJF', 'DJF'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('DZD', 'DZD'), ('EGP', 'EGP'), ('ERN', 'ERN'), ('ETB', 'ETB'), ('FJD', 'FJD'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('GHS', 'GHS'), ('GMD', 'GMD'), ('GNF', 'GNF'), ('GTQ', 'GTQ'), ('GYD', 'GYD'), ('HKD', 'HKD'), ('HNL', 'HNL'), ('HRK', 'HRK'), ('HTG', 'HTG'), ('HUF', 'HUF'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('INR', 'INR'), ('IRR', 'IRR'), ('ISK', 'ISK'), ('JMD', 'JMD'), ('JOD', 'JOD'), ('JPY', 'JPY'), ('KES', 'KES'), ('KGS', 'KGS'), ('KHR', 'KHR'), ('KMF', 'KMF'), ('KPW', 'KPW'), ('KRW', 'KRW'), ('KWD', 'KWD'), ('KYD', 'KYD'), ('KZT', 'KZT'), ('LAK', 'LAK'), ('LKR', 'LKR'), ('LRD', 'LRD'), ('LSL', 'LSL'), ('LYD', 'LYD'), ('MAD', 'MAD'), ('MDL', 'MDL'), ('MGA', 'MGA'), ('MKD', 'MKD'), ('MMK', 'MMK'), ('MNT', 'MNT'), ('MOP', 'MOP'), ('MRO', 'MRO'), ('MUR', 'MUR'), ('MVR', 'MVR'), ('MWK', 'MWK'), ('MXN', 'MXN'), ('MYR', 'MYR'), ('MZN', 'MZN'), ('NAD', 'NAD'), ('XPF', 'XPF'), ('NGN', 'NGN'), ('NIO', 'NIO'), ('NOK', 'NOK'), ('NPR', 'NPR'), ('OMR', 'OMR'), ('PEN', 'PEN'), ('PGK', 'PGK'), ('PHP', 'PHP'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('QAR', 'QAR'), ('RSD', 'RSD'), ('RUB', 'RUB'), ('RWF', 'RWF'), ('SAR', 'SAR'), ('SBD', 'SBD'), ('SCR', 'SCR'), ('SDG', 'SDG'), ('SEK', 'SEK'), ('SGD', 'SGD'), ('SHP', 'SHP'), ('SLL', 'SLL'), ('SOS', 'SOS'), ('SRD', 'SRD'), ('SSP', 'SSP'), ('STD', 'STD'), ('SYP', 'SYP'), ('SZL', 'SZL'), ('THB', 'THB'), ('TJS', 'TJS'), ('TND', 'TND'), ('TOP', 'TOP'), ('TRY', 'TRY'), ('TTD', 'TTD'), ('TWD', 'TWD'), ('TZS', 'TZS'), ('UAH', 'UAH'), ('UYU', 'UYU'), ('UZS', 'UZS'), ('VEF', 'VEF'), ('VND', 'VND'), ('VUV', 'VUV'), ('WST', 'WST'), ('YER', 'YER'), ('ZAR', 'ZAR')], max_length=3, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Commodity',
                'verbose_name_plural': 'Commodities',
                'db_table': 'commodity',
            },
        ),
        migrations.CreateModel(
            name='Customs',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'cst_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('no_eei', models.CharField(blank=True, max_length=20, null=True)),
                ('aes', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=20, null=True)),
                ('terms_of_trade', models.CharField(max_length=20)),
                ('commercial_invoice', models.BooleanField(null=True)),
            ],
            options={
                'verbose_name': 'Customs Info',
                'verbose_name_plural': 'Customs Info',
                'db_table': 'customs',
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'pcl_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('width', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('length', models.FloatField(blank=True, null=True)),
                ('packaging_type', models.CharField(blank=True, max_length=50, null=True)),
                ('package_preset', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('is_document', models.BooleanField(blank=True, default=False, null=True)),
                ('weight_unit', models.CharField(blank=True, choices=[('KG', 'KG'), ('LB', 'LB')], max_length=2, null=True)),
                ('dimension_unit', models.CharField(blank=True, choices=[('CM', 'CM'), ('IN', 'IN')], max_length=2, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Parcel',
                'verbose_name_plural': 'Parcels',
                'db_table': 'parcel',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'pyt_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('paid_by', models.CharField(blank=True, choices=[('sender', 'sender'), ('recipient', 'recipient'), ('third_party', 'third_party'), ('credit_card', 'credit_card')], max_length=20, null=True)),
                ('currency', models.CharField(blank=True, choices=[('EUR', 'EUR'), ('AED', 'AED'), ('USD', 'USD'), ('XCD', 'XCD'), ('AMD', 'AMD'), ('ANG', 'ANG'), ('AOA', 'AOA'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('AWG', 'AWG'), ('AZN', 'AZN'), ('BAM', 'BAM'), ('BBD', 'BBD'), ('BDT', 'BDT'), ('XOF', 'XOF'), ('BGN', 'BGN'), ('BHD', 'BHD'), ('BIF', 'BIF'), ('BMD', 'BMD'), ('BND', 'BND'), ('BOB', 'BOB'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('BTN', 'BTN'), ('BWP', 'BWP'), ('BYN', 'BYN'), ('BZD', 'BZD'), ('CAD', 'CAD'), ('CDF', 'CDF'), ('XAF', 'XAF'), ('CHF', 'CHF'), ('NZD', 'NZD'), ('CLP', 'CLP'), ('CNY', 'CNY'), ('COP', 'COP'), ('CRC', 'CRC'), ('CUC', 'CUC'), ('CVE', 'CVE'), ('CZK', 'CZK'), ('DJF', 'DJF'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('DZD', 'DZD'), ('EGP', 'EGP'), ('ERN', 'ERN'), ('ETB', 'ETB'), ('FJD', 'FJD'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('GHS', 'GHS'), ('GMD', 'GMD'), ('GNF', 'GNF'), ('GTQ', 'GTQ'), ('GYD', 'GYD'), ('HKD', 'HKD'), ('HNL', 'HNL'), ('HRK', 'HRK'), ('HTG', 'HTG'), ('HUF', 'HUF'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('INR', 'INR'), ('IRR', 'IRR'), ('ISK', 'ISK'), ('JMD', 'JMD'), ('JOD', 'JOD'), ('JPY', 'JPY'), ('KES', 'KES'), ('KGS', 'KGS'), ('KHR', 'KHR'), ('KMF', 'KMF'), ('KPW', 'KPW'), ('KRW', 'KRW'), ('KWD', 'KWD'), ('KYD', 'KYD'), ('KZT', 'KZT'), ('LAK', 'LAK'), ('LKR', 'LKR'), ('LRD', 'LRD'), ('LSL', 'LSL'), ('LYD', 'LYD'), ('MAD', 'MAD'), ('MDL', 'MDL'), ('MGA', 'MGA'), ('MKD', 'MKD'), ('MMK', 'MMK'), ('MNT', 'MNT'), ('MOP', 'MOP'), ('MRO', 'MRO'), ('MUR', 'MUR'), ('MVR', 'MVR'), ('MWK', 'MWK'), ('MXN', 'MXN'), ('MYR', 'MYR'), ('MZN', 'MZN'), ('NAD', 'NAD'), ('XPF', 'XPF'), ('NGN', 'NGN'), ('NIO', 'NIO'), ('NOK', 'NOK'), ('NPR', 'NPR'), ('OMR', 'OMR'), ('PEN', 'PEN'), ('PGK', 'PGK'), ('PHP', 'PHP'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('QAR', 'QAR'), ('RSD', 'RSD'), ('RUB', 'RUB'), ('RWF', 'RWF'), ('SAR', 'SAR'), ('SBD', 'SBD'), ('SCR', 'SCR'), ('SDG', 'SDG'), ('SEK', 'SEK'), ('SGD', 'SGD'), ('SHP', 'SHP'), ('SLL', 'SLL'), ('SOS', 'SOS'), ('SRD', 'SRD'), ('SSP', 'SSP'), ('STD', 'STD'), ('SYP', 'SYP'), ('SZL', 'SZL'), ('THB', 'THB'), ('TJS', 'TJS'), ('TND', 'TND'), ('TOP', 'TOP'), ('TRY', 'TRY'), ('TTD', 'TTD'), ('TWD', 'TWD'), ('TZS', 'TZS'), ('UAH', 'UAH'), ('UYU', 'UYU'), ('UZS', 'UZS'), ('VEF', 'VEF'), ('VND', 'VND'), ('VUV', 'VUV'), ('WST', 'WST'), ('YER', 'YER'), ('ZAR', 'ZAR')], max_length=3, null=True)),
                ('account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'trk_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('tracking_number', models.CharField(max_length=50, unique=True)),
                ('events', jsonfield.fields.JSONField(blank=True, default=[], null=True)),
                ('test_mode', models.BooleanField()),
                ('tracking_carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.carrier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tracking Satus',
                'verbose_name_plural': 'Tracking Statuses',
                'db_table': 'tracking-status',
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'shp_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('created', 'created'), ('cancelled', 'cancelled'), ('purchased', 'purchased')], default='created', max_length=50)),
                ('tracking_number', models.CharField(blank=True, max_length=50, null=True)),
                ('shipment_identifier', models.CharField(blank=True, max_length=50, null=True)),
                ('label', models.TextField(blank=True, null=True)),
                ('tracking_url', models.TextField(blank=True, null=True)),
                ('test_mode', models.BooleanField()),
                ('selected_rate', jsonfield.fields.JSONField(blank=True, null=True)),
                ('options', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('services', jsonfield.fields.JSONField(blank=True, default=[], null=True)),
                ('doc_images', jsonfield.fields.JSONField(blank=True, default=[], null=True)),
                ('meta', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('shipment_rates', jsonfield.fields.JSONField(blank=True, default=[], null=True)),
                ('carriers', models.ManyToManyField(blank=True, related_name='rating_carriers', to='providers.Carrier')),
                ('customs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.customs')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.payment')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to='manager.address')),
                ('selected_rate_carrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selected_rate_carrier', to='providers.carrier')),
                ('shipment_parcels', models.ManyToManyField(related_name='shipment_parcels', to='manager.Parcel')),
                ('shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipper', to='manager.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Shipment',
                'verbose_name_plural': 'Shipments',
                'db_table': 'shipment',
            },
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(purpleserver.core.models.uuid, *(), **{'prefix': 'pck_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('confirmation_number', models.CharField(max_length=50, unique=True)),
                ('test_mode', models.BooleanField()),
                ('pickup_date', models.DateField()),
                ('ready_time', models.CharField(max_length=5)),
                ('closing_time', models.CharField(max_length=5)),
                ('instruction', models.CharField(blank=True, max_length=200, null=True)),
                ('package_location', models.CharField(blank=True, max_length=200, null=True)),
                ('options', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.address')),
                ('pickup_carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.carrier')),
                ('shipments', models.ManyToManyField(related_name='pickup_shipments', to='manager.Shipment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pickup',
                'verbose_name_plural': 'Pickups',
                'db_table': 'pickup',
            },
        ),
        migrations.AddField(
            model_name='customs',
            name='duty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.payment'),
        ),
        migrations.AddField(
            model_name='customs',
            name='shipment_commodities',
            field=models.ManyToManyField(blank=True, to='manager.Commodity'),
        ),
        migrations.AddField(
            model_name='customs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
