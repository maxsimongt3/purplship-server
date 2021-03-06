import { state } from '@/library/api';
import { CarrierSettings } from '@purplship/purplship';
import React, { useState } from 'react';
import { Reference } from '@/library/context';
import InputField from '@/components/generic/input-field';
import CheckBoxField from '@/components/generic/checkbox-field';
import ButtonField from '@/components/generic/button-field';
import SelectField from './generic/select-field';
import { Connection, NotificationType } from '@/library/types';

interface ConnectProviderModalComponent {
    connection?: Connection;
    className?: string;
}

const DEFAULT_STATE: Partial<Connection> = { carrier_name: 'none', test: true };

const ConnectProviderModal: React.FC<ConnectProviderModalComponent> = ({ children, connection, className }) => {
    const [key, setKey] = useState<string>(`connection-${Date.now()}`);
    const [isNew, _] = useState<boolean>(connection === null || connection === undefined);
    const [payload, setPayload] = useState<Partial<Connection>>(connection || DEFAULT_STATE);
    const [error, setError] = useState<string>("");
    const [isActive, setIsActive] = useState<boolean>(false);
    const [isDisabled, setIsDisabled] = useState<boolean>(true);
    const [hasError, setHasError] = useState<boolean>(false);

    const handleSubmit = async (evt: React.FormEvent<HTMLFormElement>) => {
        evt.preventDefault();
        try {
            setIsDisabled(true);
            const data = {
                carrier_name: payload.carrier_name as CarrierSettings.CarrierNameEnum,
                carrier_config: payload
            };
            if (isNew) {
                await state.connectProvider(data);
            } else {
                const response = await state.updateConnection(payload.id as string, data);
                setPayload(response);
            }
            state.setNotification({
                type: NotificationType.success,
                message: `carrier connection ${isNew ? 'registered' : 'updated'} successfully`
            });
            close();
        } catch (err) {
            setHasError(true);
            setError(err.message);
            setIsDisabled(false);
        }
    };
    const close = (_?: React.MouseEvent) => {
        if (isNew) setPayload(DEFAULT_STATE);
        setKey(`connection-${Date.now()}`);
        setHasError(false);
        setIsDisabled(false);
        setIsActive(false);
    };
    const handleOnChange = (property: string) => (e: React.ChangeEvent<any>) => {
        let new_state = { ...payload, [property]: e.target.value || undefined };
        if (property === 'carrier_name') {
            setKey(`connection-${Date.now()}`);
            new_state = { carrier_name: e.target.value, test: true };
        } else if (property == 'test') {
            new_state = { ...payload, test: e.target.checked };
        }
        setPayload(new_state);
        setIsDisabled((connection || DEFAULT_STATE) == new_state);
    };
    const has = (property: string) => {
        return hasProperty(payload.carrier_name as CarrierSettings.CarrierNameEnum, property);
    };

    return (
        <>
            <button className={className} onClick={() => setIsActive(true)}>
                {children}
            </button>

            <div className={`modal ${isActive ? "is-active" : ""}`} key={key}>
                <div className="modal-background" onClick={close}></div>
                <form className="modal-card" onSubmit={handleSubmit}>
                    <section className="modal-card-body">
                        <h3 className="subtitle is-3">{isNew ? 'Connect a Carrier' : 'Update a Carrier Connection'}</h3>
                        <p className="is-size-7 has-text-danger my-1" style={{ visibility: (hasError ? "visible" : "hidden") }}>{error}</p>

                        <SelectField value={payload.carrier_name} onChange={handleOnChange("carrier_name")} disabled={!isNew} key={`select-${key}`} className="is-fullwidth" required>
                            <option value='none'>Select Carrier</option>

                            <Reference.Consumer>
                                {(ref) => (Object.values(ref || {}).length > 0) && Object.keys(ref.carriers).map(carrier => (
                                    <option key={carrier} value={carrier}>{ref.carriers[carrier]}</option>
                                ))}
                            </Reference.Consumer>

                        </SelectField>

                        {(payload.carrier_name !== 'none' && has("carrier_id")) &&
                            <>
                                <hr />

                                <InputField label="Carrier Id" defaultValue={payload.carrier_id} onChange={handleOnChange("carrier_id")} className="is-small" required />

                                {/* Carrier specific fields BEGING */}

                                {has("site_id") && <InputField label="Site Id" defaultValue={payload.site_id} onChange={handleOnChange("site_id")} className="is-small" required />}

                                {has("sendle_id") && <InputField label="Sendle ID" defaultValue={payload.sendle_id} onChange={handleOnChange("sendle_id")} className="is-small" required />}

                                {has("api_key") && <InputField label="API Key" defaultValue={payload.api_key} onChange={handleOnChange("api_key")} className="is-small" required />}

                                {has("client_id") && <InputField label="Client ID" defaultValue={payload.client_id} onChange={handleOnChange("client_id")} className="is-small" required />}

                                {has("partner_id") && <InputField label="Partner ID" defaultValue={payload.partner_id} onChange={handleOnChange("partner_id")} className="is-small" required />}

                                {has("check_word") && <InputField label="Check Word" defaultValue={payload.check_word} onChange={handleOnChange("check_word")} className="is-small" required />}

                                {has("username") && <InputField label="Username" defaultValue={payload.username} onChange={handleOnChange("username")} className="is-small" required />}

                                {has("password") && <InputField label="Password" defaultValue={payload.password} onChange={handleOnChange("password")} className="is-small" required />}

                                {has("client_secret") && <InputField label="Client Secret" defaultValue={payload.client_secret} onChange={handleOnChange("client_secret")} className="is-small" required />}

                                {has("customer_number") && <InputField label="Customer Number" defaultValue={payload.customer_number} onChange={handleOnChange("customer_number")} className="is-small" required />}

                                {has("license_key") && <InputField label="License Key" defaultValue={payload.license_key} onChange={handleOnChange("license_key")} className="is-small" />}

                                {has("consumer_key") && <InputField label="Consumer Key" defaultValue={payload.consumer_key} onChange={handleOnChange("consumer_key")} className="is-small" required />}

                                {has("consumer_secret") && <InputField label="Consumer Secret" defaultValue={payload.consumer_secret} onChange={handleOnChange("consumer_secret")} className="is-small" required />}

                                {has("contract_id") && <InputField label="Contract Id" defaultValue={payload.contract_id} onChange={handleOnChange("contract_id")} className="is-small" required />}

                                {has("api_secret") && <InputField label="API Secret" defaultValue={payload.api_secret} onChange={handleOnChange("api_secret")} className="is-small" required />}

                                {has("account_number") && <InputField label="Account Number" defaultValue={payload.account_number} onChange={handleOnChange("account_number")} className="is-small" required />}

                                {has("billing_account") && <InputField label="Billing Account" defaultValue={payload.billing_account} onChange={handleOnChange("billing_account")} className="is-small" />}

                                {has("meter_number") && <InputField label="Meter Number" defaultValue={payload.meter_number} onChange={handleOnChange("meter_number")} className="is-small" required />}

                                {has("user_key") && <InputField label="User Key" defaultValue={payload.user_key} onChange={handleOnChange("user_key")} className="is-small" />}

                                {has("user_token") && <InputField label="User Token" defaultValue={payload.user_token} onChange={handleOnChange("user_token")} className="is-small" required />}

                                {has("access_license_number") && <InputField label="Access License Number" defaultValue={payload.access_license_number} onChange={handleOnChange("access_license_number")} className="is-small" required />}

                                {has("account_pin") && <InputField label="Account Pin" defaultValue={payload.account_pin} onChange={handleOnChange("account_pin")} className="is-small" required />}

                                {has("account_entity") && <InputField label="Account Entity" defaultValue={payload.account_entity} onChange={handleOnChange("account_entity")} className="is-small" required />}

                                {has("account_country_code") && <InputField label="Account Country Code" defaultValue={payload.account_country_code} onChange={handleOnChange("account_country_code")} className="is-small" required />}

                                {/* Carrier specific fields END */}

                                <CheckBoxField defaultChecked={payload.test} onChange={handleOnChange("test")}>Test Mode</CheckBoxField>

                                <ButtonField className="mt-2" fieldClass="has-text-centered" disabled={isDisabled}>Submit</ButtonField>
                            </>
                        }
                    </section>
                </form>
                <button className="modal-close is-large" aria-label="close" onClick={close}></button>
            </div>
        </>
    )
};

function hasProperty(carrier_name: CarrierSettings.CarrierNameEnum, property: string): boolean {
    // TODO: Use carriers settings types when available for automatic validation
    return ({
        [CarrierSettings.CarrierNameEnum.Aramex]: ["carrier_id", "test", "username", "password", "account_pin", "account_entity", "account_number", "account_country_code"],
        [CarrierSettings.CarrierNameEnum.Australiapost]: ["carrier_id", "test", "api_key", "password", "account_number"],
        [CarrierSettings.CarrierNameEnum.Canadapost]: ["carrier_id", "test", "username", "password", "customer_number", "contract_id"],
        [CarrierSettings.CarrierNameEnum.Canpar]: ["carrier_id", "test", "username", "password"],
        [CarrierSettings.CarrierNameEnum.Dicom]: ["carrier_id", "test", "username", "password", "billing_account"],
        [CarrierSettings.CarrierNameEnum.DhlExpress]: ["carrier_id", "test", "site_id", "password", "account_number"],
        [CarrierSettings.CarrierNameEnum.DhlUniversal]: ["carrier_id", "test", "consumer_key", "consumer_secret"],
        [CarrierSettings.CarrierNameEnum.Eshipper]: ["carrier_id", "test", "username", "password"],
        [CarrierSettings.CarrierNameEnum.Freightcom]: ["carrier_id", "test", "username", "password"],
        [CarrierSettings.CarrierNameEnum.FedexExpress]: ["carrier_id", "test", "user_key", "password", "meter_number", "account_number"],
        [CarrierSettings.CarrierNameEnum.PurolatorCourier]: ["carrier_id", "test", "username", "password", "account_number", "user_token"],
        [CarrierSettings.CarrierNameEnum.Royalmail]: ["carrier_id", "test", "client_id", "client_secret"],
        [CarrierSettings.CarrierNameEnum.Sendle]: ["carrier_id", "test", "sendle_id", "api_key"],
        [CarrierSettings.CarrierNameEnum.SfExpress]: ["carrier_id", "test", "partner_id", "check_word"],
        [CarrierSettings.CarrierNameEnum.UpsPackage]: ["carrier_id", "test", "username", "password", "access_license_number", "account_number"],
        [CarrierSettings.CarrierNameEnum.Usps]: ["carrier_id", "test", "username", "password"],
        [CarrierSettings.CarrierNameEnum.Yanwen]: ["carrier_id", "test", "customer_number", "license_key"],
        [CarrierSettings.CarrierNameEnum.Yunexpress]: ["carrier_id", "test", "customer_number", "api_secret"]
    }[carrier_name] || []).includes(property)
}

export default ConnectProviderModal;