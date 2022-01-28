from typing import Any, List

from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.templating import Jinja2Templates
from saleor_app.deps import (
    ConfigurationFormDeps,
    get_settings,
    saleor_domain_header,
    verify_saleor_domain,
    verify_webhook_signature,
    webhook_event_type,
)
from saleor_app.errors import InstallAppError
from saleor_app.graphql import GraphQLError
from saleor_app.install import install_app
from saleor_app.schemas.core import InstallData
from saleor_app.schemas.manifest import Manifest


async def manifest(request: Request, settings=Depends(get_settings)):
    manifest = settings.manifest.dict(by_alias=True)
    manifest["appUrl"] = ""
    manifest["tokenTargetUrl"] = request.url_for("app-install")
    manifest["configurationUrl"] = request.url_for("configuration-form")
    manifest["extensions"] = [
        {
            "label": "Create with Plugin #1",
            "mount": "PRODUCT_OVERVIEW_CREATE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Create with Plugin #2",
            "mount": "PRODUCT_OVERVIEW_CREATE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Create with Plugin #3 - app page",
            "mount": "PRODUCT_OVERVIEW_CREATE",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
        {
            "label": "Product list plugin #1",
            "mount": "PRODUCT_OVERVIEW_MORE_ACTIONS",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Product list plugin #2",
            "mount": "PRODUCT_OVERVIEW_MORE_ACTIONS",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Product list plugin #3 - app page",
            "mount": "PRODUCT_OVERVIEW_MORE_ACTIONS",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
        {
            "label": "Product details plugin #1",
            "mount": "PRODUCT_DETAILS_MORE_ACTIONS",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Product details plugin #2",
            "mount": "PRODUCT_DETAILS_MORE_ACTIONS",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Product details plugin #3 - app page",
            "mount": "PRODUCT_DETAILS_MORE_ACTIONS",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
        {
            "label": "Catalog navi #1",
            "mount": "NAVIGATION_CATALOG",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Catalog navi #2 - app_page",
            "mount": "NAVIGATION_CATALOG",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
        {
            "label": "Orders navi #1",
            "mount": "NAVIGATION_ORDERS",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Orders navi #2 - app_page",
            "mount": "NAVIGATION_ORDERS",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
        {
            "label": "Customers navi #1",
            "mount": "NAVIGATION_CUSTOMERS",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Customers navi #2 - app_page",
            "mount": "NAVIGATION_CUSTOMERS",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
        {
            "label": "Discounts navi #1",
            "mount": "NAVIGATION_DISCOUNTS",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Discounts navi #2 - app_page",
            "mount": "NAVIGATION_DISCOUNTS",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
        {
            "label": "Translations navi #1",
            "mount": "NAVIGATION_TRANSLATIONS",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Translations navi #2 - app_page",
            "mount": "NAVIGATION_TRANSLATIONS",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
        {
            "label": "Pages navi #1",
            "mount": "NAVIGATION_PAGES",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": request.url_for("configuration-form"),
        },
        {
            "label": "Pages navi #2 - app_page",
            "mount": "NAVIGATION_PAGES",
            "target": "APP_PAGE",
            "permissions": [
                "MANAGE_PRODUCTS",
            ],
            "url": "/configuration/",
        },
    ]
    return Manifest(**manifest)


async def install(
    request: Request,
    # data: InstallData,
    # _domain_is_valid=Depends(verify_saleor_domain),
    # saleor_domain=Depends(saleor_domain_header),
):
    # target_url = request.url_for("handle-webhook")
    # domain = saleor_domain
    # auth_token = data.auth_token
    # try:
    #     await install_app(
    #         domain,
    #         auth_token,
    #         request.app.extra["saleor"]["webhook_handlers"].get_assigned_events(),
    #         target_url,
    #         request.app.extra["saleor"]["save_app_data"],
    #     )
    # except (InstallAppError, GraphQLError):
    #     raise HTTPException(
    #         status_code=403, detail="Incorrect token or not enough permissions"
    #     )

    return {}


async def handle_webhook(
    request: Request,
    payload: List[Any],  # FIXME provide a way to proper define payload types
    _domain_is_valid=Depends(verify_saleor_domain),
    saleor_domain=Depends(saleor_domain_header),
    event_type=Depends(webhook_event_type),
    _signature_is_valid=Depends(verify_webhook_signature),
):
    response = {}
    handler = request.app.extra["saleor"]["webhook_handlers"].get(event_type)
    if handler is not None:
        response = await handler(payload, saleor_domain)
    return response or {}


async def get_form(commons: ConfigurationFormDeps = Depends()):
    context = {
        "request": commons.request,
        "form_url": commons.request.url,
        "domain": commons.saleor_domain,
        "token": commons.token,
    }
    return Jinja2Templates(directory=str(commons.settings.static_dir)).TemplateResponse(
        "configuration/index.html", context
    )
